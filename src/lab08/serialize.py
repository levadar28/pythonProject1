import json
from typing import List, Optional
from models import Student


def students_to_json(students: List[Student], path: str) -> None:
    """
    Сохраняет список студентов в JSON-файл.

    Args:
        students: Список объектов Student
        path: Путь к файлу для сохранения

    Raises:
        TypeError: Если передан не список или элементы не являются Student
        IOError: При ошибках записи в файл
    """
    if not isinstance(students, list):
        raise TypeError(f"Ожидается список, получен {type(students).__name__}")

    # Проверяю тип всех элементов
    for i, student in enumerate(students):
        if not isinstance(student, Student):
            raise TypeError(
                f"Элемент с индексом {i} не является объектом Student, "
                f"получен {type(student).__name__}"
            )

    # Сериализую всех студентов
    data = [student.to_dict() for student in students]

    # Записываю в файл
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        raise IOError(f"Ошибка записи в файл {path}: {str(e)}")


def students_from_json(path: str) -> List[Student]:
    """
    Читает JSON-массив из файла и создаёт список объектов Student.

    Args:
        path: Путь к JSON-файлу

    Returns:
        Список объектов Student

    Raises:
        IOError: При ошибках чтения файла
        json.JSONDecodeError: При невалидном JSON
        ValueError: При ошибках валидации данных студентов
        KeyError: При отсутствии обязательных полей
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except IOError as e:
        raise IOError(f"Ошибка чтения файла {path}: {str(e)}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Некорректный JSON в файле {path}",
            e.doc,
            e.pos
        )

    if not isinstance(data, list):
        raise TypeError(
            f"Ожидается JSON-массив, получен {type(data).__name__}"
        )

    students = []
    errors = []

    for i, item in enumerate(data):
        try:
            # Проверяю, что элемент является словарем
            if not isinstance(item, dict):
                raise TypeError(
                    f"Элемент с индексом {i} должен быть словарем, "
                    f"получен {type(item).__name__}"
                )

            # Создаю объект Student
            student = Student.from_dict(item)
            students.append(student)

        except (ValueError, TypeError, KeyError) as e:
            error_msg = f"Ошибка в элементе {i}: {str(e)}"
            errors.append(error_msg)

    # Если были ошибки при создании студентов, выбрасываю исключение
    if errors:
        error_summary = "\n".join(errors)
        raise ValueError(
            f"Не удалось создать всех студентов из файла {path}.\n"
            f"Ошибки:\n{error_summary}"
        )

    return students


# Пример использования
if __name__ == "__main__":
    # Создаю тестовых студентов
    test_students = [
        Student(
            fio="Иванов Иван Иванович",
            birthdate="2000-05-15",
            group="SE-01",
            gpa=4.2
        ),
        Student(
            fio="Петрова Мария Сергеевна",
            birthdate="2001-03-22",
            group="SE-02",
            gpa=4.8
        ),
        Student(
            fio="Сидоров Алексей Викторович",
            birthdate="1999-11-30",
            group="CS-01",
            gpa=3.9
        )
    ]

    # Тестирую сохранение в JSON
    print("Тестируем сохранение в JSON...")
    try:
        students_to_json(test_students, "students.json")
        print("Файл students.json успешно создан")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

    # Тестирую чтение из JSON
    print("\nТестируем чтение из JSON...")
    try:
        loaded_students = students_from_json("students.json")
        print(f"Успешно загружено {len(loaded_students)} студентов:")

        for student in loaded_students:
            print(f"- {student.fio} ({student.group}), GPA: {student.gpa}")

    except Exception as e:
        print(f"Ошибка при загрузке: {e}")

    # Тестирую обработку ошибок
    print("\nТестируем обработку ошибок...")

    # 1. Невалидный JSON
    try:
        with open("invalid.json", "w") as f:
            f.write("{это не валидный json}")
        students_from_json("invalid.json")
    except Exception as e:
        print(f"1. Невалидный JSON: {type(e).__name__}: {e}")

    # 2. JSON с неверной структурой (не список)
    try:
        with open("not_list.json", "w", encoding="utf-8") as f:
            json.dump({"name": "test"}, f)
        students_from_json("not_list.json")
    except Exception as e:
        print(f"2. JSON не список: {type(e).__name__}: {e}")

    # 3. JSON с неполными данными
    try:
        incomplete_data = [
            {"fio": "Тест", "birthdate": "2000-01-01", "group": "SE-01"},
            # отсутствует поле gpa
        ]
        with open("incomplete.json", "w", encoding="utf-8") as f:
            json.dump(incomplete_data, f)
        students_from_json("incomplete.json")
    except Exception as e:
        print(f"3. Неполные данные: {type(e).__name__}: {e}")

    # 4. JSON с невалидными данными
    try:
        invalid_data = [
            {"fio": "Тест", "birthdate": "не дата", "group": "SE-01", "gpa": 4.0}
        ]
        with open("invalid_data.json", "w", encoding="utf-8") as f:
            json.dump(invalid_data, f)
        students_from_json("invalid_data.json")
    except Exception as e:
        print(f"4. Невалидные данные: {type(e).__name__}: {e}")