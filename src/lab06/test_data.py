import os
import json


def create_simple_test_data():
    """Создает тестовые файлы прямо в папке lab06 для простоты"""

    # Создаем папки прямо здесь
    os.makedirs("test_data/samples", exist_ok=True)
    os.makedirs("test_data/out", exist_ok=True)

    print("Создаем тестовые файлы в папке test_data/")

    # Создаем people.csv
    csv_content = """name,age,city
Иван,25,Москва
Мария,30,Санкт-Петербург
Петр,35,Казань
Анна,28,Новосибирск
Сергей,32,Екатеринбург"""

    with open("test_data/samples/people.csv", "w", encoding="utf-8") as f:
        f.write(csv_content)
    print("Создан: test_data/samples/people.csv")

    # Создаем people.txt
    txt_content = """Это тестовый файл для демонстрации работы утилиты.
Файл содержит несколько строк текста на русском языке.
Мы будем анализировать частоты слов в этом тексте.
Текст текст текст - повторяющиеся слова должны быть найдены.
Это предложение содержит слова для статистического анализа."""

    with open("test_data/samples/people.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)
    print("Создан: test_data/samples/people.txt")

    # Создаем data.json
    json_data = [
        {"name": "Иван", "age": 25, "city": "Москва"},
        {"name": "Мария", "age": 30, "city": "Санкт-Петербург"},
        {"name": "Петр", "age": 35, "city": "Казань"},
    ]

    with open("test_data/samples/data.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    print("Создан: test_data/samples/data.json")

    print("\nТестовые файлы успешно созданы в папке test_data/")
    print("\nПримеры команд:")
    print('  python cli_convert.py cat --input "test_data/samples/people.csv" -n')
    print(
        '  python cli_convert.py stats --input "test_data/samples/people.txt" --top 5'
    )
    print(
        '  python cli_convert.py json2csv --in "test_data/samples/data.json" --out "test_data/out/data.csv"'
    )
    print(
        '  python cli_convert.py csv2json --in "test_data/samples/people.csv" --out "test_data/out/people.json"'
    )


if __name__ == "__main__":
    create_simple_test_data()
