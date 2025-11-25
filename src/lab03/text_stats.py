import sys
import re
from collections import Counter


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализация текста"""
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        text = text.casefold()
    text = re.sub(r"[\t\r\n]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str) -> list[str]:
    """Разбивка на слова"""
    pattern = r"\b[\w-]+\b"
    tokens = re.findall(pattern, text)
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчет частоты"""
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Топ-N слов"""
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


def main():
    # Чтение одной строки
    text = sys.stdin.readline().strip()
    print(f"DEBUG: Получен текст: '{text}'")  # Отладочная информация

    if not text:
        print("Всего слов: 0")
        print("Уникальных слов: 0")
        print("Топ-5:")
        return

    normalized_text = normalize(text)
    print(f"DEBUG: После нормализации: '{normalized_text}'")

    tokens = tokenize(normalized_text)
    print(f"DEBUG: Токены: {tokens}")

    total_words = len(tokens)
    unique_words = len(set(tokens))
    freq_dict = count_freq(tokens)
    top_words = top_n(freq_dict, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
