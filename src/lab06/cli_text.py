import argparse
from collections import Counter
import os
import sys


def read_file(file_path):
    """Чтение файла с проверкой его существования"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def cat_command(input_file, number_lines=False):
    """Реализация команды cat с нумерацией строк"""
    lines = read_file(input_file)
    for i, line in enumerate(lines, 1):
        if number_lines:
            print(f"{i:6d}\t{line.rstrip()}")
        else:
            print(line.rstrip())


def stats_command(input_file, top_n=5):
    """Реализация команды stats с подсчетом частоты слов"""
    lines = read_file(input_file)
    words = []
    for line in lines:
        # Более аккуратная обработка слов - убираем пунктуацию
        line_words = line.strip().lower().split()
        cleaned_words = [word.strip('.,!?;:"()[]') for word in line_words]
        words.extend(cleaned_words)

    # Убираем пустые строки
    words = [word for word in words if word]

    counter = Counter(words)
    most_common = counter.most_common(top_n)

    print(f"Топ-{top_n} самых частых слов:")
    for i, (word, count) in enumerate(most_common, 1):
        print(f"{i:2d}. {word:<15} {count:>3} раз(а)")


def main():
    parser = argparse.ArgumentParser(
        description="CLI‑утилиты лабораторной №6",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python cli_text.py cat --input example.txt
  python cli_text.py cat --input example.txt -n
  python cli_text.py stats --input example.txt
  python cli_text.py stats --input example.txt --top 10
        """,
    )

    subparsers = parser.add_subparsers(
        dest="command", title="доступные команды", metavar="команда"
    )

    # Подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="нумеровать строки")

    # Подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="статистика частот слов")
    stats_parser.add_argument("--input", required=True, help="путь к входному файлу")
    stats_parser.add_argument(
        "--top", type=int, default=5, help="количество топ-слов (по умолчанию: 5)"
    )

    args = parser.parse_args()

    if not args.command:
        # Если команда не указана, показываем справку
        parser.print_help()
        return

    try:
        if args.command == "cat":
            cat_command(args.input, args.n)
        elif args.command == "stats":
            stats_command(args.input, args.top)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
