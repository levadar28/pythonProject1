from openpyxl import Workbook
import csv
from pathlib import Path

# Создаем директории
Path("data/samples").mkdir(parents=True, exist_ok=True)
Path("data/out").mkdir(parents=True, exist_ok=True)

# Сначала создаем CSV файл
with open("data/samples/people.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])  # заголовок
    writer.writerow(["Alice", "22", "SPB"])
    writer.writerow(["Bob", "25", "Moscow"])
    writer.writerow(["Charlie", "30", "London"])

print("CSV файл создан: data/samples/people.csv")

# Теперь создаем Excel из CSV
wb = Workbook()
ws = wb.active
ws.title = "Sheet1"

with open("data/samples/people.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        ws.append(row)  # Добавляем каждую строку из CSV в Excel

    wb.save("data/out/people.xlsx")

print("Excel файл создан: data/out/people.xlsx")

# Проверяем содержимое
print("\nСодержимое CSV файла:")
with open("data/samples/people.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
