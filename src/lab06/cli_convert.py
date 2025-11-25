import argparse
import sys
import os
import json
import csv
from collections import Counter
import re


def read_file(filename):
    """Чтение файла с обработкой ошибок"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден: {os.path.abspath(filename)}")
        print(f"Текущая директория: {os.getcwd()}")
        print("Доступные файлы в текущей директории:")
        for item in os.listdir("."):
            print(f"  - {item}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")
        sys.exit(1)


def write_file(filename, content, mode="w"):
    """Запись файла с обработкой ошибок"""
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, mode, encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Ошибка при записи файла {filename}: {e}")
        sys.exit(1)


def cat_command(input_file, number_lines):
    """Команда cat - вывод содержимого файла"""
    lines = read_file(input_file)
    for i, line in enumerate(lines, 1):
        if number_lines:
            print(f"{i:6d}\t{line.rstrip()}")
        else:
            print(line.rstrip())


def stats_command(input_file, top_n):
    """Команда stats - статистика частот слов"""
    if top_n <= 0:
        print("Ошибка: параметр --top должен быть положительным числом")
        sys.exit(1)

    lines = read_file(input_file)
    text = " ".join(lines)

    # Разбивка на слова с игнорированием регистра
    words = re.findall(r"\b\w+\b", text.lower())

    if not words:
        print("Файл не содержит слов")
        return

    # Подсчет частот
    counter = Counter(words)

    # Вывод топ-N
    print(f"Топ-{top_n} самых частых слов:")
    for word, count in counter.most_common(top_n):
        print(f"{word}: {count}")


def json_to_csv(input_file, output_file):
    """Конвертация JSON в CSV"""
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            print("Предупреждение: JSON файл пуст")
            return

        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            # Список словарей
            fieldnames = data[0].keys() if data else []
            with open(output_file, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            print(f"Успешно: {input_file} -> {output_file}")
        else:
            print("Ошибка: JSON должен содержать список словарей")
            sys.exit(1)

    except json.JSONDecodeError as e:
        print(f"Ошибка: Неверный формат JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при конвертации JSON в CSV: {e}")
        sys.exit(1)


def csv_to_json(input_file, output_file):
    """Конвертация CSV в JSON"""
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Успешно: {input_file} -> {output_file}")

    except csv.Error as e:
        print(f"Ошибка: Неверный формат CSV: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при конвертации CSV в JSON: {e}")
        sys.exit(1)


def csv_to_xlsx(input_file, output_file):
    """Конвертация CSV в XLSX (заглушка - требует внешней библиотеки)"""
    print(
        "Ошибка: Конвертация CSV в XLSX требует установки внешней библиотеки (openpyxl или xlsxwriter)"
    )
    print("Установите библиотеку: pip install openpyxl")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="CLI‑утилиты для работы с файлами и конвертации данных",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Простые примеры использования:
  python cli_convert.py cat --input "test_data/samples/people.csv" -n
  python cli_convert.py stats --input "test_data/samples/people.txt" --top 5
  python cli_convert.py json2csv --in "test_data/samples/data.json" --out "test_data/out/data.csv"
  python cli_convert.py csv2json --in "test_data/samples/people.csv" --out "test_data/out/people.json"
        """,
    )

    subparsers = parser.add_subparsers(
        dest="command", title="доступные команды", help="выберите команду"
    )

    # Подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # Подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Статистика частот слов")
    stats_parser.add_argument("--input", required=True, help="Входной файл")
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Количество топ-слов (по умолчанию: 5)"
    )

    # Подкоманда json2csv
    json2csv_parser = subparsers.add_parser(
        "json2csv", help="Конвертировать JSON в CSV"
    )
    json2csv_parser.add_argument(
        "--in", dest="input", required=True, help="Входной JSON файл"
    )
    json2csv_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной CSV файл"
    )

    # Подкоманда csv2json
    csv2json_parser = subparsers.add_parser(
        "csv2json", help="Конвертировать CSV в JSON"
    )
    csv2json_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV файл"
    )
    csv2json_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной JSON файл"
    )

    # Подкоманда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx", help="Конвертировать CSV в XLSX (требует openpyxl)"
    )
    csv2xlsx_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV файл"
    )
    csv2xlsx_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной XLSX файл"
    )

    args = parser.parse_args()

    # Если команда не указана, показать помощь
    if not args.command:
        parser.print_help()
        return

    # Выполнение команд
    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)
    elif args.command == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)


if __name__ == "__main__":
    main()
