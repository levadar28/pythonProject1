import os
import json
from models import Student


def create_example_files():
    """Создает примеры файлов JSON в директории data/lab08/"""

    # Создаю директорию, если она не существует
    os.makedirs("data/lab08", exist_ok=True)

    # Пример данных для входного файла
    students_data = [
        {
            "fio": "Иванов Иван Иванович",
            "birthdate": "2000-05-15",
            "group": "SE-01",
            "gpa": 4.2
        },
        {
            "fio": "Петрова Мария Сергеевна",
            "birthdate": "2001-03-22",
            "group": "SE-02",
            "gpa": 4.8
        },
        {
            "fio": "Сидоров Алексей Викторович",
            "birthdate": "1999-11-30",
            "group": "CS-01",
            "gpa": 3.9
        },
        {
            "fio": "Козлова Анна Дмитриевна",
            "birthdate": "2002-07-14",
            "group": "AI-01",
            "gpa": 4.5
        },
        {
            "fio": "Николаев Денис Сергеевич",
            "birthdate": "2000-12-03",
            "group": "SE-01",
            "gpa": 3.2
        }
    ]

    # Создаю входной файл
    input_path = "data/lab08/students_input.json"
    with open(input_path, "w", encoding="utf-8") as f:
        json.dump(students_data, f, ensure_ascii=False, indent=2)
    print(f"Создан файл: {input_path}")

    # Читаю входной файл и создаю из него объекты Student
    with open(input_path, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)

    # Создаю список объектов Student
    students = []
    for data in loaded_data:
        student = Student.from_dict(data)
        students.append(student)

    # Создаю выходной файл (результат сериализации)
    output_path = "data/lab08/students_output.json"
    output_data = [student.to_dict() for student in students]

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"Создан файл: {output_path}")

    # Также создаю пример файла с ошибками для тестирования
    error_data = [
        {
            "fio": "Тестовый Студент",
            "birthdate": "неправильная-дата",  # ошибка формата
            "group": "TEST-01",
            "gpa": 4.0
        }
    ]

    error_path = "data/lab08/students_error.json"
    with open(error_path, "w", encoding="utf-8") as f:
        json.dump(error_data, f, ensure_ascii=False, indent=2)
    print(f"Создан тестовый файл с ошибкой: {error_path}")

    # Создаю пример пустого списка
    empty_path = "data/lab08/students_empty.json"
    with open(empty_path, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)
    print(f"Создан файл с пустым списком: {empty_path}")


if __name__ == "__main__":
    create_example_files()
    print("\nПримеры файлов созданы в директории data/lab08/")
    print("\nСтруктура файлов:")
    print("-" * 40)
    print("students_input.json   - входные данные для загрузки")
    print("students_output.json  - результат сериализации")
    print("students_error.json   - пример с ошибкой (для тестирования)")
    print("students_empty.json   - пустой список (для тестирования)")