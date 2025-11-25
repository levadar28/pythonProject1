import pytest
import json
import csv
import os
from src.lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    """Тесты для функции json_to_csv"""

    def test_basic_conversion(self, tmp_path):
        """Тест базовой конвертации JSON -> CSV"""
        # Создаю тестовый JSON файл
        json_data = [
            {"name": "Alice", "age": 30, "city": "New York"},
            {"name": "Bob", "age": 25, "city": "London"},
            {"name": "Charlie", "age": 35, "city": "Tokyo"},
        ]

        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"

        with open(json_file, "w") as f:
            json.dump(json_data, f)

        # Выполняю конвертацию
        json_to_csv(str(json_file), str(csv_file))

        # Проверяю результат
        assert csv_file.exists()

        with open(csv_file, "r", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Проверяю количество записей
        assert len(rows) == len(json_data)

        # Проверяю заголовки
        expected_headers = ["name", "age", "city"]
        assert reader.fieldnames == expected_headers

        # Проверяю данные
        for i, row in enumerate(rows):
            assert row["name"] == json_data[i]["name"]
            assert row["age"] == str(json_data[i]["age"])  # CSV сохраняет как строки
            assert row["city"] == json_data[i]["city"]

    def test_different_data_types(self, tmp_path):
        """Тест с различными типами данных"""
        json_data = [
            {
                "string": "text",
                "number": 42,
                "float": 3.14,
                "boolean": True,
                "null": None,
            }
        ]

        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"

        with open(json_file, "w") as f:
            json.dump(json_data, f)

        json_to_csv(str(json_file), str(csv_file))

        with open(csv_file, "r", newline="") as f:
            reader = csv.DictReader(f)
            row = next(reader)

        # Проверяю, что все значения преобразованы в строки
        assert row["string"] == "text"
        assert row["number"] == "42"
        assert row["float"] == "3.14"
        assert row["boolean"] == "True"  # Изменено на "True" (с большой буквы)
        assert row["null"] == ""  # null становится пустой строкой

    def test_empty_json_array(self, tmp_path):
        """Тест с пустым JSON массивом - теперь ожидаем ошибку"""
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"

        with open(json_file, "w") as f:
            json.dump([], f)

        # Ожидаю ошибку, т.к. функция не допускает пустой массив
        with pytest.raises(ValueError, match="JSON файл пуст"):
            json_to_csv(str(json_file), str(csv_file))

    def test_missing_keys(self, tmp_path):
        """Тест с объектами, у которых разные ключи"""
        json_data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "city": "London"},  # нет age
            {"age": 25, "city": "Tokyo"},  # нет name
        ]

        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"

        with open(json_file, "w") as f:
            json.dump(json_data, f)

        json_to_csv(str(json_file), str(csv_file))

        with open(csv_file, "r", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Все возможные ключи должны быть в заголовках
        expected_headers = ["name", "age", "city"]
        assert set(reader.fieldnames) == set(expected_headers)

        # Проверяю, что отсутствующие значения - пустые строки
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "30"
        assert rows[0]["city"] == ""

        assert rows[1]["name"] == "Bob"
        assert rows[1]["age"] == ""
        assert rows[1]["city"] == "London"

    def test_nonexistent_json_file(self):
        """Тест с несуществующим JSON файлом"""
        with pytest.raises(FileNotFoundError):
            json_to_csv("nonexistent.json", "output.csv")

    def test_invalid_json_file(self, tmp_path):
        """Тест с некорректным JSON"""
        json_file = tmp_path / "test.json"

        # Записываю некорректный JSON
        with open(json_file, "w") as f:
            f.write('{"invalid": json}')

        with pytest.raises(ValueError):
            json_to_csv(str(json_file), "output.csv")

    def test_empty_json_file(self, tmp_path):
        """Тест с пустым JSON файлом"""
        json_file = tmp_path / "test.json"

        # Создаю пустой файл
        json_file.write_text("")

        with pytest.raises(ValueError):
            json_to_csv(str(json_file), "output.csv")


class TestCsvToJson:
    """Тесты для функции csv_to_json"""

    def test_basic_conversion(self, tmp_path):
        """Тест базовой конвертации CSV -> JSON"""
        # Создаю тестовый CSV-файл
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "test.json"

        with open(csv_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
            writer.writeheader()
            writer.writerow({"name": "Alice", "age": "30", "city": "New York"})
            writer.writerow({"name": "Bob", "age": "25", "city": "London"})
            writer.writerow({"name": "Charlie", "age": "35", "city": "Tokyo"})

        # Выполняю конвертацию
        csv_to_json(str(csv_file), str(json_file))

        # Проверяю результат
        assert json_file.exists()

        with open(json_file, "r") as f:
            json_data = json.load(f)

        # Проверяю количество записей
        assert len(json_data) == 3

        # Проверяю структуру данных
        expected_data = [
            {"name": "Alice", "age": "30", "city": "New York"},
            {"name": "Bob", "age": "25", "city": "London"},
            {"name": "Charlie", "age": "35", "city": "Tokyo"},
        ]

        for i, item in enumerate(json_data):
            assert item == expected_data[i]

    def test_empty_csv_file(self, tmp_path):
        """Тест с пустым CSV файлом (только заголовок) - теперь ожидаем ошибку"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "test.json"

        # CSV только с заголовком
        with open(csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "age"])

        # Ожидаю ошибку, так как функция не допускает CSV без данных
        with pytest.raises(ValueError, match="CSV файл пуст"):
            csv_to_json(str(csv_file), str(json_file))

    def test_csv_with_different_data_types(self, tmp_path):
        """Тест CSV с различными типами данных как строки"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "test.json"

        with open(csv_file, "w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["string", "number", "float", "boolean"]
            )
            writer.writeheader()
            writer.writerow(
                {"string": "text", "number": "42", "float": "3.14", "boolean": "true"}
            )

        csv_to_json(str(csv_file), str(json_file))

        with open(json_file, "r") as f:
            json_data = json.load(f)

        # Все значения остаются строками (CSV не сохраняет типы)
        assert json_data[0]["string"] == "text"
        assert json_data[0]["number"] == "42"
        assert json_data[0]["float"] == "3.14"
        assert json_data[0]["boolean"] == "true"

    def test_nonexistent_csv_file(self):
        """Тест с несуществующим CSV файлом"""
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")

    def test_csv_with_malformed_data(self, tmp_path):
        """Тест с CSV с проблемными данными (некорректные кавычки)"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "test.json"

        # Создаю CSV с проблемными данными
        with open(csv_file, "w", newline="") as f:
            f.write("name,description\n")
            f.write('test,"unclosed quote\n')  # Незакрытая кавычка

        # В зависимости от реализации это может вызвать ошибку или нет
        # Если функция использует стандартный csv.reader, он может обработать это
        try:
            csv_to_json(str(csv_file), str(json_file))
            # Если не вызвало исключение, проверяю, что файл создан
            assert json_file.exists()
        except ValueError:
            # Или ожидаю ValueError
            pass

    def test_empty_csv_without_headers(self, tmp_path):
        """Тест с полностью пустым CSV файлом"""
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("")  # Абсолютно пустой файл

        with pytest.raises(ValueError):
            csv_to_json(str(csv_file), "output.json")


class TestRoundTrip:
    """Тесты на полный цикл конвертации JSON -> CSV -> JSON"""

    def test_round_trip_conversion(self, tmp_path):
        """Тест полного цикла конвертации"""
        original_data = [
            {"name": "Alice", "age": 30, "active": True},
            {"name": "Bob", "age": 25, "active": False},
            {"name": "Charlie", "age": 35, "active": True},
        ]

        # Сохраняю оригинальный JSON
        original_json = tmp_path / "original.json"
        with open(original_json, "w") as f:
            json.dump(original_data, f)

        # JSON -> CSV
        intermediate_csv = tmp_path / "intermediate.csv"
        json_to_csv(str(original_json), str(intermediate_csv))

        # CSV -> JSON
        final_json = tmp_path / "final.json"
        csv_to_json(str(intermediate_csv), str(final_json))

        # Загружаю результат
        with open(final_json, "r") as f:
            final_data = json.load(f)

        # Проверяю, что количество записей совпадает
        assert len(final_data) == len(original_data)

        # Проверяю, что ключи совпадают
        original_keys = set(original_data[0].keys())
        final_keys = set(final_data[0].keys())
        assert original_keys == final_keys

        # Примечание: типы данных могут измениться (числа -> строки, boolean -> строки)
        # Это нормально для CSV формата


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
