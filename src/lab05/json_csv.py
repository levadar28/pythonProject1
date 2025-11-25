import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
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

    # Проверка структуры данных
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    if not data:
        raise ValueError("JSON файл пуст")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    # Определение колонок (порядок из первого объекта + алфавитная сортировка остальных)
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())

    # Порядок: сначала ключи из первого объекта, затем остальные в алфавитном порядке
    first_item_keys = list(data[0].keys()) if data else []
    remaining_keys = sorted(all_keys - set(first_item_keys))
    fieldnames = first_item_keys + remaining_keys

    # Запись CSV
    try:
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for row in data:
                # Заполняем отсутствующие поля пустыми строками
                complete_row = {key: row.get(key, "") for key in fieldnames}
                # Преобразуем все значения в строки
                complete_row = {
                    k: str(v) if v is not None else "" for k, v in complete_row.items()
                }
                writer.writerow(complete_row)

    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
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

            # Проверка наличия заголовка
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовка")

            data = list(reader)

    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")

    # Проверка на пустой CSV
    if not data:
        raise ValueError("CSV файл пуст")

    # Запись JSON
    try:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")
