import json
import csv
from pathlib import Path

# Создаем структуру папок
Path("data/samples").mkdir(parents=True, exist_ok=True)
Path("data/out").mkdir(parents=True, exist_ok=True)

# Создаем пример people.json
people_data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]

# Записываем исходный JSON
with open("data/samples/people.json", "w", encoding="utf-8") as f:
    json.dump(people_data, f, ensure_ascii=False, indent=2)

print("Создан data/samples/people.json")
