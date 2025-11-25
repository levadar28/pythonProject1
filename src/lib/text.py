import re
from typing import List, Dict, Tuple


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""

    normalized = text

    if casefold:
        normalized = normalized.casefold()

    if yo2e:
        if casefold:
            normalized = normalized.replace("ё", "е")
        else:
            normalized = normalized.replace("ё", "е").replace("Ё", "Е")

    normalized = re.sub(r"\s+", " ", normalized)

    return normalized.strip()


def tokenize(text: str) -> List[str]:
    if not text:
        return []

    tokens = re.findall(r"\b\w+(?:-\w+)*\b", text, re.UNICODE)

    return tokens


def count_freq(tokens: List[str]) -> Dict[str, int]:

    freq_dict = {}

    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1

    return freq_dict


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    if not freq:
        return []

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return sorted_items[:n]


print(repr(normalize("ПрИвЕт\nМИр\t")))
print(repr(normalize("ёжик, Ёлка", yo2e=True)))
print(repr(normalize("Hello\r\nWorld")))
print(repr(normalize("  двойные   пробелы  ")))

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

tokens1 = ["a", "b", "a", "c", "b", "a"]
freq1 = count_freq(tokens1)
print(freq1)
print(top_n(freq1, 2))

tokens2 = ["bb", "aa", "bb", "aa", "cc"]
freq2 = count_freq(tokens2)
print(freq2)
print(top_n(freq2, 2))


import re
from collections import Counter


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализация текста
    """
    # Замена ё на е
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    # Приведение к нижнему регистру (casefold)
    if casefold:
        text = text.casefold()

    # Замена управляющих символов на пробелы
    text = re.sub(r"[\t\r\n]", " ", text)

    # Схлопывание множественных пробелов и удаление пробелов по краям
    text = re.sub(r"\s+", " ", text).strip()

    return text


def tokenize(text: str) -> list[str]:
    """
    Разбивка текста на токены (слова)
    """
    # Регулярное выражение: буквы/цифры/подчеркивание + дефис внутри слова
    pattern = r"\b[\w-]+\b"
    tokens = re.findall(pattern, text)

    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    Подсчет частоты токенов
    """
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает топ-N слов по частоте
    """
    # Сортировка: сначала по убыванию частоты, затем по алфавиту
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
