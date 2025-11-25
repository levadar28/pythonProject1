import csv
from pathlib import Path

rows = [
    {"name": "Alice", "age": "22", "city": "SPB"},
    {"name": "Bob", "age": "25", "city": "Moscow"},
]

# Запись данных в CSV
with open("data/out/people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()  # Записываем заголовок
    writer.writerows(rows)  # Записываем все строки

# Чтение данных из CSV
with open("data/out/people.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
