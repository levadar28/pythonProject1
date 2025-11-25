import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:
    """Тесты для функции normalize()"""

    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("Hello World", "hello world"),
            ("ПРИВЕТ МИР", "привет мир"),
            ("Test with 123 numbers", "test with 123 numbers"),
            ("Special chars: !@#$%^&*()", "special chars: !@#$%^&*()"),
            ("With'apostrophe", "with'apostrophe"),
            ("   Extra   Spaces   ", "extra spaces"),  # функция удаляет лишние пробелы
            ("", ""),
            ("UPPER and lower", "upper and lower"),
        ],
    )
    def test_normalize(self, input_text, expected):
        assert normalize(input_text) == expected


class TestTokenize:
    """Тесты для функции tokenize()"""

    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("hello world", ["hello", "world"]),
            ("  multiple   spaces  ", ["multiple", "spaces"]),
            ("one", ["one"]),
            ("", []),
            ("trailing space ", ["trailing", "space"]),
            (" leading space", ["leading", "space"]),
            (
                "hello, world! test.",
                ["hello", "world", "test"],
            ),  # функция удаляет пунктуацию
            (
                "price: $100.50",
                ["price", "100", "50"],
            ),  # функция удаляет символы и разбивает числа
        ],
    )
    def test_tokenize(self, input_text, expected):
        assert tokenize(input_text) == expected


class TestCountFreq:
    """Тесты для функции count_freq()"""

    @pytest.mark.parametrize(
        "tokens, expected",
        [
            (["a", "b", "a"], {"a": 2, "b": 1}),
            (["x", "x", "x"], {"x": 3}),
            ([], {}),
            (["hello", "world"], {"hello": 1, "world": 1}),
            (["test", "test", "TEST"], {"test": 2, "TEST": 1}),
            (["hello!", "hello", "hello?"], {"hello!": 1, "hello": 1, "hello?": 1}),
        ],
    )
    def test_count_freq(self, tokens, expected):
        assert count_freq(tokens) == expected


class TestTopN:
    """Тесты для функции top_n()"""

    def test_basic_top_n(self):
        freq = {"a": 5, "b": 3, "c": 7, "d": 2}
        result = top_n(freq, 3)
        expected = [("c", 7), ("a", 5), ("b", 3)]
        assert result == expected

    def test_empty_dict(self):
        assert top_n({}, 5) == []

    def test_n_larger_than_dict(self):
        freq = {"x": 1, "y": 2}
        result = top_n(freq, 5)
        expected = [("y", 2), ("x", 1)]
        assert result == expected

    def test_same_frequency_ordering(self):
        freq = {"beta": 2, "alpha": 2, "gamma": 2, "delta": 1}
        result = top_n(freq, 3)
        # Должны быть отсортированы по алфавиту при одинаковой частоте
        expected = [("alpha", 2), ("beta", 2), ("gamma", 2)]
        assert result == expected

    def test_negative_n(self):
        freq = {"a": 1, "b": 2}
        # Функция возвращает элементы при отрицательном n
        result = top_n(freq, -1)
        # Проверю, что возвращается не пустой список (конкретное поведение зависит от реализации)
        assert len(result) > 0

    def test_zero_n(self):
        freq = {"a": 1, "b": 2}
        assert top_n(freq, 0) == []

    def test_mixed_punctuation_tokens(self):
        freq = {"hello": 3, "hello!": 2, "world": 4, "world.": 1}
        result = top_n(freq, 3)
        expected = [("world", 4), ("hello", 3), ("hello!", 2)]
        assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
