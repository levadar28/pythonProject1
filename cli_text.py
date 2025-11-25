import argparse
from collections import Counter
import os
import sys


def read_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def cat_command(input_file, number_lines=False):
    lines = read_file(input_file)
    for i, line in enumerate(lines, 1):
        if number_lines:
            print(f"{i:6d}\t{line.rstrip()}")
        else:
            print(line.rstrip())


def stats_command(input_file, top_n=5):
    lines = read_file(input_file)
    words = []
    for line in lines:
        line_words = line.strip().lower().split()
        cleaned_words = [word.strip('.,!?;:"()[]') for word in line_words]
        words.extend(cleaned_words)

    words = [word for word in words if word]
    counter = Counter(words)
    most_common = counter.most_common(top_n)

    print(f"Топ-{top_n} самых частых слов:")
    for i, (word, count) in enumerate(most_common, 1):
        print(f"{i:2d}. {word:<15} {count:>3} раз(а)")


def main():
    parser = argparse.ArgumentParser(description="CLI утилиты")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true")

    stats_parser = subparsers.add_parser("stats", help="статистика частот слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    try:
        if args.command == "cat":
            cat_command(args.input, args.n)
        elif args.command == "stats":
            stats_command(args.input, args.top)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
