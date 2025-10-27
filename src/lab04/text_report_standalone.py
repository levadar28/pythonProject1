#!/usr/bin/env python3
"""
Скрипт анализа текста без внешних зависимостей.
"""

import sys
from pathlib import Path
import csv
import re
from collections import Counter


def read_text_with_encodings(path: str | Path) -> str:
    """
    Читает файл, пробуя разные кодировки.
    """
    p = Path(path)

    if not p.exists():
        raise FileNotFoundError(f"Файл {p} не найден")

    # Список кодировок для попытки (в порядке вероятности)
    encodings_to_try = [
        'utf-8',
        'utf-16',
        'utf-16-le',
        'utf-16-be',
        'cp1251',
        'windows-1251',
        'cp866',
        'koi8-r',
        'iso-8859-1',
        'iso-8859-5'
    ]

    for encoding in encodings_to_try:
        try:
            content = p.read_text(encoding=encoding)
            print(f"✅ Успешно прочитано с кодировкой: {encoding}")
            return content
        except UnicodeDecodeError:
            continue

    # Если ни одна кодировка не подошла, пробуем с игнорированием ошибок
    try:
        content = p.read_text(encoding='utf-8', errors='ignore')
        print("⚠️  Файл прочитан с игнорированием ошибок кодировки")
        return content
    except Exception as e:
        raise UnicodeDecodeError(
            f"Не удалось прочитать файл. Попробованы кодировки: {', '.join(encodings_to_try)}") from e


def write_csv(rows: list[tuple], path: str | Path, header: tuple = None) -> None:
    """Записывает данные в CSV"""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)


def normalize(text: str) -> str:
    """Нормализует текст: casefold + ё→е"""
    text = text.lower()
    text = text.replace('ё', 'е')
    return ' '.join(text.split())


def tokenize(text: str) -> list[str]:
    """Токенизирует текст: \w+(?:-\w+)*"""
    return re.findall(r'\w+(?:-\w+)*', text)


def create_test_file():
    """Создает тестовый файл в правильной кодировке UTF-8"""
    test_file = Path("data/input.txt")
    test_file.parent.mkdir(exist_ok=True)

    test_content = "Привет, мир! Привет!!!"
    test_file.write_text(test_content, encoding="utf-8")
    print(f"✅ Создан тестовый файл: {test_file}")
    print(f"📝 Содержимое: '{test_content}'")

    return test_content


def main():
    """Основная функция"""

    print("🔍 АНАЛИЗ ТЕКСТА")
    print("=" * 50)

    input_file = Path("data/input.txt")
    output_file = Path("data/report.csv")

    # Если файла нет - создаем его
    if not input_file.exists():
        print("📝 Создаю тестовый файл...")
        create_test_file()
    else:
        print(f"📁 Найден файл: {input_file}")

    try:
        # Чтение файла
        print(f"📖 Чтение файла...")
        text = read_text_with_encodings(input_file)

        # Анализ текста
        print("🔍 Анализ текста...")
        normalized = normalize(text)
        tokens = tokenize(normalized)
        freq = Counter(tokens)
        sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        # Сохранение отчета
        if freq:
            write_csv(sorted_words, output_file, header=("word", "count"))
            print(f"💾 Отчет сохранен: {output_file}")
        else:
            write_csv([], output_file, header=("word", "count"))
            print("💾 Создан отчет с заголовком (файл пустой)")

        # Вывод результатов в формате тест-кейсов
        print(f"\nВсего слов: {sum(freq.values())}")
        print(f"Уникальных слов: {len(freq)}")

        if freq:
            print("Топ-5:")
            for word, count in sorted_words[:5]:
                print(f"{word}:{count}")

        print("=" * 50)
        print("✅ Анализ завершен успешно!")

        # Показываем содержимое CSV
        if output_file.exists():
            print(f"\n📄 Содержимое {output_file}:")
            print(output_file.read_text(encoding="utf-8"))

    except FileNotFoundError as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"❌ Ошибка кодировки: {e}")
        print("\n💡 Решение: Удалите файл data/input.txt и запустите скрипт снова")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()