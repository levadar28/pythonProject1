import json, csv
from pathlib import Path

# Создаем директории если их нет
Path("data/samples").mkdir(parents=True, exist_ok=True)
Path("data/out").mkdir(parents=True, exist_ok=True)

# Сначала создаем sample JSON файл если его нет
sample_data = [
    {"name": "Alice", "age": 22, "city": "SPB"},
    {"name": "Bob", "age": 25, "city": "Moscow"},
    {"name": "Charlie", "age": 30, "city": "London"}
]

with open("data/samples/people.json", "w", encoding="utf-8") as f:
    json.dump(sample_data, f, ensure_ascii=False, indent=2)

# Теперь читаем JSON и записываем в CSV
with open("data/samples/people.json", encoding="utf-8") as jf:
    data = json.load(jf)  # Загружаем данные из JSON

with open("data/out/people_from_json.csv", "w", newline="", encoding="utf-8") as cf:
    # Получаем все уникальные ключи из данных
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())

    # Сортируем ключи для consistent порядка колонок
    fieldnames = sorted(all_keys)

    writer = csv.DictWriter(cf, fieldnames=fieldnames)
    writer.writeheader()  # Записываем заголовок

    for row in data:
        # Заполняем отсутствующие поля пустыми строками
        complete_row = {key: str(row.get(key, '')) for key in fieldnames}
        writer.writerow(complete_row)

print("JSON → CSV преобразование завершено!")
print("Создан файл: data/out/people_from_json.csv")