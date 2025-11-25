import csv
from pathlib import Path
from typing import Union, List, Tuple


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    """
    Читает содержимое текстового файла и возвращает его как одну строку.

    Args:
        path: Путь к файлу для чтения
        encoding: Кодировка файла. По умолчанию "utf-8".
                 Для русских текстов в Windows может потребоваться "cp1251"

    Returns:
        str: Содержимое файла как одна строка

    Raises:
        FileNotFoundError: Если файл не существует
        UnicodeDecodeError: Если не удается декодировать файл в указанной кодировке
    """
    path = Path(path)

    with open(path, "r", encoding=encoding) as file:
        content = file.read()

    return content


def write_csv(
    rows: List[Union[Tuple, List]],
    path: Union[str, Path],
    header: Tuple[str, ...] = None,
) -> None:
    """
    Записывает данные в CSV файл с разделителем запятая.

    Args:
        rows: Список строк данных (каждая строка - tuple или list)
        path: Путь для сохранения CSV файла
        header: Опциональный заголовок для CSV файла

    Raises:
        ValueError: Если строки имеют разную длину
        OSError: Если невозможно записать файл
    """
    path = Path(path)

    ensure_parent_dir(path)

    if rows:
        first_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_length:
                raise ValueError(
                    f"Все строки должны иметь одинаковую длину. "
                    f"Строка {i} имеет длину {len(row)}, ожидается {first_length}. "
                    f"Строка: {row}"
                )

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)


def ensure_parent_dir(path: Union[str, Path]) -> None:
    """
    Создает родительские директории для указанного пути, если они не существуют.

    Args:
        path: Путь к файлу или директории
    """
    path = Path(path)
    parent_dir = path.parent

    if not parent_dir.exists():
        parent_dir.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    print("=== Тестирование модуля io_txt_csv ===\n")

    try:
        # Подготовка тестовых данных
        test_dir = Path("test_data")
        test_dir.mkdir(exist_ok=True)

        print("1. Тестирование read_text():")

        # Создаем тестовые файлы
        (test_dir / "input.txt").write_text(
            "Привет, мир!\nВторая строка.", encoding="utf-8"
        )
        (test_dir / "empty.txt").write_text("", encoding="utf-8")

        # Тест чтения обычного файла
        content = read_text(test_dir / "input.txt")
        print(f"✓ input.txt: {repr(content)}")

        # Тест чтения пустого файла
        empty_content = read_text(test_dir / "empty.txt")
        print(f"✓ empty.txt: {repr(empty_content)}")

        print("\n2. Тестирование write_csv():")

        # Тест с данными и заголовком
        data = [("word", "count"), ("test", 3)]
        write_csv(data, test_dir / "check.csv")
        print("✓ check.csv создан")

        # Тест только с заголовком
        write_csv([], test_dir / "header_only.csv", header=("a", "b"))
        print("✓ header_only.csv создан")

        # Тест полностью пустого CSV
        write_csv([], test_dir / "empty.csv")
        print("✓ empty.csv создан")

        print("\n3. Тестирование ensure_parent_dir():")
        ensure_parent_dir(test_dir / "deep" / "nested" / "file.txt")
        print("✓ Родительские директории созданы")

        # Очистка
        import shutil

        shutil.rmtree(test_dir)
        if Path("deep").exists():
            shutil.rmtree("deep")

        print("\n✅ Все тесты пройдены успешно!")

    except Exception as e:
        print(f"❌ Ошибка при тестировании: {e}")
        raise
