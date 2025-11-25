import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV с валидацией.
    """
    # Проверка существования файла
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")

    # Проверка расширения файла
    if json_file.suffix.lower() != ".json":
        raise ValueError(
            f"Неверный тип файла: ожидается .json, получен {json_file.suffix}"
        )

    # Чтение JSON
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {e}")

    # Валидация структуры JSON
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    # Сохраняем количество записей для проверки
    original_count = len(data)

    # Определение колонок
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())

    first_item_keys = list(data[0].keys()) if data else []
    remaining_keys = sorted(all_keys - set(first_item_keys))
    fieldnames = first_item_keys + remaining_keys

    # Запись CSV
    try:
        Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            written_count = 0
            for row in data:
                complete_row = {key: str(row.get(key, "")) for key in fieldnames}
                writer.writerow(complete_row)
                written_count += 1

        # Проверка количества записей
        if written_count != original_count:
            raise ValueError(
                f"Количество записей не совпадает: было {original_count}, записано {written_count}"
            )

    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON с валидацией.
    """
    # Проверка существования файла
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

    # Проверка расширения файла
    if csv_file.suffix.lower() != ".csv":
        raise ValueError(
            f"Неверный тип файла: ожидается .csv, получен {csv_file.suffix}"
        )

    # Чтение CSV
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            # Проверка заголовка
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовка")

            data = list(reader)

    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")

    # Валидация CSV
    if not data:
        raise ValueError("CSV файл пуст")

    # Сохраняем количество записей для проверки
    original_count = len(data)

    # Запись JSON
    try:
        Path(json_path).parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # Проверка: читаем обратно и сравниваем количество
        with open(json_path, "r", encoding="utf-8") as f:
            verify_data = json.load(f)

        if len(verify_data) != original_count:
            raise ValueError(
                f"Количество записей не совпадает: было {original_count}, стало {len(verify_data)}"
            )

    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")


# Тестирование валидации
def test_validation():
    """Тестируем различные сценарии ошибок"""

    # Создаем тестовые данные
    Path("data/samples").mkdir(parents=True, exist_ok=True)
    Path("data/out").mkdir(parents=True, exist_ok=True)

    # 1. Корректный JSON
    valid_data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    with open("data/samples/valid.json", "w", encoding="utf-8") as f:
        json.dump(valid_data, f, ensure_ascii=False, indent=2)

    # 2. Пустой JSON
    with open("data/samples/empty.json", "w", encoding="utf-8") as f:
        json.dump([], f)

    # 3. JSON с не-словарями
    invalid_data = [{"name": "Alice"}, "not_a_dict", {"name": "Bob"}]
    with open("data/samples/invalid.json", "w", encoding="utf-8") as f:
        json.dump(invalid_data, f)

    # 4. Пустой CSV
    with open("data/samples/empty.csv", "w", encoding="utf-8", newline="") as f:
        pass

    # 5. CSV без заголовка
    with open("data/samples/no_header.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Alice", "22"])
        writer.writerow(["Bob", "25"])

    # Тестируем сценарии
    test_cases = [
        ("data/samples/valid.json", "data/out/valid.csv", "Корректный JSON", True),
        ("data/samples/empty.json", "data/out/empty.csv", "Пустой JSON", False),
        (
            "data/samples/invalid.json",
            "data/out/invalid.csv",
            "JSON с не-словарями",
            False,
        ),
        (
            "data/samples/nonexistent.json",
            "data/out/none.csv",
            "Несуществующий JSON",
            False,
        ),
        ("data/samples/valid.csv", "data/out/valid.json", "Корректный CSV", True),
        ("data/samples/empty.csv", "data/out/empty.json", "Пустой CSV", False),
        (
            "data/samples/no_header.csv",
            "data/out/no_header.json",
            "CSV без заголовка",
            False,
        ),
    ]

    for input_path, output_path, description, should_succeed in test_cases:
        try:
            if input_path.endswith(".json"):
                json_to_csv(input_path, output_path)
            else:
                csv_to_json(input_path, output_path)

            if should_succeed:
                print(f"✓ {description}: УСПЕХ")
            else:
                print(f"✗ {description}: ОШИБКА (должен был завершиться с ошибкой)")

        except (ValueError, FileNotFoundError) as e:
            if not should_succeed:
                print(f"✓ {description}: ОЖИДАЕМАЯ ОШИБКА - {e}")
            else:
                print(f"✗ {description}: НЕОЖИДАННАЯ ОШИБКА - {e}")


if __name__ == "__main__":
    test_validation()
