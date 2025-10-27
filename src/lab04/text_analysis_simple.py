#!/usr/bin/env python3
"""
Все тест-кейсы в одном скрипте без зависимостей.
"""

from pathlib import Path
import csv
import re
from collections import Counter


def process_test_case(test_name, input_text, expected_output):
    """Обрабатывает один тест-кейс"""
    print(f"\n{'=' * 60}")
    print(f"ТЕСТ-КЕЙС {test_name}")
    print(f"Вход: '{input_text}'")
    print('=' * 60)

    # Нормализация: casefold + ё→е
    normalized = input_text.lower().replace('ё', 'е')
    normalized = ' '.join(normalized.split())

    # Токенизация: \w+(?:-\w+)*
    tokens = re.findall(r'\w+(?:-\w+)*', normalized)

    # Подсчет частот
    freq = Counter(tokens)

    # Сортировка: count ↓, word ↑
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Сохранение CSV
    filename = f"data/report_{test_name.lower()}.csv"
    Path("data").mkdir(exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        if sorted_words:
            writer.writerows(sorted_words)

    # Вывод результатов
    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")

    if freq:
        print("Топ-5:")
        for word, count in sorted_words[:5]:
            print(f"{word}:{count}")
    else:
        print("Топ-5: нет данных")

    # Проверка ожидаемого результата
    print(f"\n✅ РЕЗУЛЬТАТ:")
    actual_output = dict(sorted_words)
    print(f"Получено: {actual_output}")
    print(f"Ожидалось: {expected_output}")

    if actual_output == expected_output:
        print("🎯 ТЕСТ ПРОЙДЕН!")
    else:
        print("❌ ТЕСТ НЕ ПРОЙДЕН!")

    # Показываем файл
    print(f"💾 Файл: {filename}")
    print(Path(filename).read_text(encoding="utf-8"))


def main():
    """Запуск всех тест-кейсов"""

    print("🎯 ЗАПУСК ТЕСТ-КЕЙСОВ ДЛЯ АНАЛИЗА ТЕКСТА")
    print("Создаю необходимые файлы...")

    # Тест-кейс A: Базовый случай
    process_test_case(
        "A",
        "Привет, мир! Привет!!!",
        {"привет": 2, "мир": 1}
    )

    # Тест-кейс B: Пустой файл
    process_test_case(
        "B",
        "",
        {}
    )

    # Тест-кейс C: Простой текст
    process_test_case(
        "C",
        "Привет",
        {"привет": 1}
    )

    


if __name__ == "__main__":
    main()