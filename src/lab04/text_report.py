#!/usr/bin/env python3
"""
Скрипт для анализа текста и генерации отчета частот слов.

Читает текстовый файл, анализирует частоты слов и создает CSV отчет.
"""

import sys
import argparse
from pathlib import Path
from collections import Counter

# Импорты из модулей проекта
try:
    from src.lab04.io_txt_csv import read_text, write_csv
    from src.lab03.text1 import normalize, tokenize
except ImportError:
    # Резервные импорты для случаев проблем с путями
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))
    from src.lab04.io_txt_csv import read_text, write_csv
    from src.lab03.text1 import normalize, tokenize


def calculate_word_frequencies(text: str) -> dict[str, int]:
    """
    Вычисляет частоты слов в тексте.

    Args:
        text: Исходный текст для анализа

    Returns:
        Словарь {слово: частота}
    """
    if not text.strip():
        return {}

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    return Counter(tokens)


def get_top_words(freq: dict[str, int], n: int = None) -> list[tuple[str, int]]:
    """
    Возвращает слова, отсортированные по убыванию частоты.

    Args:
        freq: Словарь частот
        n: Количество слов для возврата (None = все слова)

    Returns:
        Список кортежей (слово, частота), отсортированных по частоте ↓, слову ↑
    """
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:n] if n is not None else sorted_words


def generate_report(
    input_file: Path, output_file: Path, encoding: str = "cp1251"
) -> bool:
    """
    Генерирует отчет по анализу текста.

    Args:
        input_file: Путь к входному файлу
        output_file: Путь для сохранения отчета
        encoding: Кодировка файла

    Returns:
        True если успешно, False при ошибке
    """
    try:
        # Чтение входного файла
        print(f"📖 Чтение файла: {input_file} (кодировка: {encoding})")
        text = read_text(input_file, encoding=encoding)

        # Анализ текста
        print("🔍 Анализ текста...")
        frequencies = calculate_word_frequencies(text)
        total_words = sum(frequencies.values())
        unique_words = len(frequencies)

        # Подготовка данных для CSV
        if frequencies:
            sorted_words = get_top_words(frequencies)
            write_csv(sorted_words, output_file, header=("word", "count"))
            print(f"💾 Отчет сохранен: {output_file}")
        else:
            # Пустой файл - создаем только заголовок
            write_csv([], output_file, header=("word", "count"))
            print("💾 Создан пустой отчет (только заголовок)")

        # Вывод статистики
        print("\n" + "=" * 40)
        print("📊 СТАТИСТИКА АНАЛИЗА ТЕКСТА")
        print("=" * 40)
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")

        if frequencies:
            top_5 = get_top_words(frequencies, 5)
            print("\n🏆 Топ-5 самых частых слов:")
            for i, (word, count) in enumerate(top_5, 1):
                print(f"  {i}. '{word}' - {count}")
        else:
            print("\n📭 Текст не содержит слов для анализа")
        print("=" * 40)

        return True

    except FileNotFoundError:
        print(f"❌ Ошибка: файл '{input_file}' не найден")
        return False
    except UnicodeDecodeError as e:
        print(f"❌ Ошибка кодировки: {e}")
        print("💡 Попробуйте указать другую кодировку: --encoding cp1251")
        return False
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return False


def main():
    """Основная функция скрипта."""
    parser = argparse.ArgumentParser(
        description="Анализ текста и генерация отчета частот слов",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  %(prog)s                                  # использует пути по умолчанию
  %(prog.py --in data/in.txt --out out.csv  # пользовательские пути
  %(prog)s --encoding cp1251               # для файлов из Windows
  %(prog)s -i text.txt -o report.csv -e windows-1251

Краевые случаи:
  • Если входной файл не существует - ошибка с кодом выхода 1
  • Если файл пустой - создается отчет только с заголовком
  • Проблемы с кодировкой - подсказка использовать --encoding
        """,
    )

    parser.add_argument(
        "-i",
        "--in",
        dest="input_file",
        default="data/input.txt",
        help="Путь к входному текстовому файлу (по умолчанию: data/input.txt)",
    )

    parser.add_argument(
        "-o",
        "--out",
        dest="output_file",
        default="data/report.csv",
        help="Путь для сохранения CSV отчета (по умолчанию: data/report.csv)",
    )

    parser.add_argument(
        "-e",
        "--encoding",
        dest="encoding",
        default="utf-8",
        help="Кодировка входного файла (по умолчанию: utf-8). Для Windows файлов используйте cp1251",
    )

    parser.add_argument("--verbose", "-v", action="store_true", help="Подробный вывод")

    args = parser.parse_args()

    if args.verbose:
        print("🚀 Запуск анализа текста...")
        print(f"   Входной файл: {args.input_file}")
        print(f"   Выходной файл: {args.output_file}")
        print(f"   Кодировка: {args.encoding}")

    # Проверка и подготовка путей
    input_path = Path(args.input_file)
    output_path = Path(args.output_file)

    # Создание директории для выходного файла
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Запуск генерации отчета
    success = generate_report(input_path, output_path, args.encoding)

    if success:
        if args.verbose:
            print(f"✅ Задание выполнено успешно!")
        sys.exit(0)
    else:
        if args.verbose:
            print(f"❌ Задание завершено с ошибками")
        sys.exit(1)


if __name__ == "__main__":
    main()
