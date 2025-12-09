import csv
import os
import statistics
from datetime import datetime
from typing import List, Dict, Any, Optional


class Student:
    """Вспомогательный класс для представления студента"""

    def __init__(self, fio: str, birthdate: str, group: str, gpa: str):
        self.fio = fio
        self.birthdate = birthdate
        self.group = group
        self.gpa = float(gpa)  # Преобразую в float для вычислений

    def __repr__(self):
        return f"Student(fio='{self.fio}', birthdate='{self.birthdate}', group='{self.group}', gpa={self.gpa})"

    def to_dict(self) -> Dict[str, str]:
        """Конвертирует объект Student в словарь"""
        return {
            'fio': self.fio,
            'birthdate': self.birthdate,
            'group': self.group,
            'gpa': str(self.gpa)  # Обратно в строку
        }


class Group:
    """Класс для работы с группой студентов, хранящейся в CSV-файле"""

    # Ожидаемые заголовки CSV файла
    HEADER = ['fio', 'birthdate', 'group', 'gpa']

    def __init__(self, storage_path: str):
        """
        Инициализация группы и файла-хранилища

        Args:
            storage_path: путь к CSV-файлу с данными студентов
        """
        self.path = storage_path
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """Создает файл с заголовком, если его ещё нет"""
        if not os.path.exists(self.path):
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.HEADER)
                writer.writeheader()

    def _read_all(self) -> List[Dict[str, str]]:
        """Читает все строки из CSV и возвращает список словарей"""
        students = []
        with open(self.path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        return students

    def list(self) -> List[Student]:
        """Возвращает всех студентов в виде списка объектов Student"""
        students_data = self._read_all()
        return [Student(**data) for data in students_data]

    def stats(self) -> Dict[str, Any]:
        """
        Собирает статистику по студентам

        Returns:
            Словарь со статистикой:
            {
                "count": общее количество студентов,
                "min_gpa": минимальный gpa,
                "max_gpa": максимальный gpa,
                "avg_gpa": средний gpa,
                "groups": распределение по группам {группа: количество},
                "top_5_students": топ-5 студентов с самым высоким GPA
            }
        """
        students = self.list()

        if not students:
            # Если студентов нет, возвращаю пустую статистику
            return {
                "count": 0,
                "min_gpa": 0.0,
                "max_gpa": 0.0,
                "avg_gpa": 0.0,
                "groups": {},
                "top_5_students": []
            }

        # Базовая статистика
        gpa_values = [student.gpa for student in students]

        # Распределение по группам
        groups_distribution = {}
        for student in students:
            group_name = student.group
            groups_distribution[group_name] = groups_distribution.get(group_name, 0) + 1

        # Топ-5 студентов по GPA
        sorted_students = sorted(students, key=lambda x: x.gpa, reverse=True)
        top_5 = [
            {"fio": student.fio, "gpa": student.gpa}
            for student in sorted_students[:5]
        ]

        # Расчет медианы GPA (дополнительно)
        median_gpa = statistics.median(gpa_values) if len(gpa_values) >= 1 else 0.0

        # Расчет моды групп (дополнительно)
        if groups_distribution:
            most_common_group = max(groups_distribution.items(), key=lambda x: x[1])
        else:
            most_common_group = ("Нет данных", 0)

        # Расчет стандартного отклонения GPA (дополнительно)
        if len(gpa_values) > 1:
            std_dev_gpa = statistics.stdev(gpa_values)
        else:
            std_dev_gpa = 0.0

        # Возвращаю основную и расширенную статистику
        return {
            # Основная статистика (по заданию)
            "count": len(students),
            "min_gpa": min(gpa_values),
            "max_gpa": max(gpa_values),
            "avg_gpa": sum(gpa_values) / len(gpa_values),
            "groups": groups_distribution,
            "top_5_students": top_5,

            # Дополнительная статистика
            "median_gpa": median_gpa,
            "std_dev_gpa": std_dev_gpa,
            "most_common_group": most_common_group[0],
            "students_in_most_common_group": most_common_group[1],
            "gpa_range": max(gpa_values) - min(gpa_values)
        }

    def add(self, student: Student) -> None:
        """Добавляет нового студента в CSV файл"""
        with open(self.path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.HEADER)
            writer.writerow(student.to_dict())

    def find(self, substr: str) -> List[Student]:
        """Находит студентов по подстроке в ФИО"""
        all_students = self.list()
        substr_lower = substr.lower()
        return [s for s in all_students if substr_lower in s.fio.lower()]

    def remove(self, fio: str) -> int:
        """Удаляет запись(и) с данным ФИО"""
        all_students = self.list()
        students_to_keep = [s for s in all_students if s.fio != fio]
        removed_count = len(all_students) - len(students_to_keep)

        if removed_count > 0:
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.HEADER)
                writer.writeheader()
                for student in students_to_keep:
                    writer.writerow(student.to_dict())

        return removed_count

    def update(self, fio: str, **fields: Any) -> int:
        """Обновляет поля существующего студента"""
        all_students = self.list()
        updated_count = 0

        for student in all_students:
            if student.fio == fio:
                updated_count += 1
                for field, value in fields.items():
                    if field in self.HEADER:
                        setattr(student, field, str(value))

        if updated_count > 0:
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.HEADER)
                writer.writeheader()
                for student in all_students:
                    writer.writerow(student.to_dict())

        return updated_count


# Демонстрация работы метода stats()
def demonstrate_stats():
    """Функция для демонстрации работы метода stats()"""

    # Создаю тестовый файл
    test_file = "test_students.csv"

    # Удаляю файл, если он существует
    if os.path.exists(test_file):
        os.remove(test_file)

    # Создаю группу
    group = Group(test_file)

    # Добавляю тестовых студентов
    test_students = [
        Student("Иванов Иван Иванович", "2000-05-15", "БИВТ-21-1", "4.5"),
        Student("Петров Петр Петрович", "2001-03-20", "БИВТ-21-1", "3.8"),
        Student("Сидорова Анна Сергеевна", "1999-11-30", "БИВТ-21-2", "4.2"),
        Student("Кузнецов Алексей Дмитриевич", "2000-07-22", "БИВТ-21-3", "3.5"),
        Student("Смирнова Екатерина Владимировна", "2001-01-10", "БИВТ-21-2", "4.7"),
        Student("Васильев Василий Васильевич", "2000-12-05", "БИВТ-21-1", "4.9"),
        Student("Николаева Ольга Игоревна", "2001-04-18", "БИВТ-21-3", "3.9"),
        Student("Алексеев Дмитрий Сергеевич", "1999-08-25", "БИВТ-21-2", "4.0"),
        Student("Павлова Мария Андреевна", "2000-02-14", "БИВТ-21-1", "4.3"),
        Student("Федоров Артем Викторович", "2001-06-30", "БИВТ-21-3", "3.6"),
    ]

    for student in test_students:
        group.add(student)

    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ МЕТОДА stats()")
    print("=" * 60)

    # Получаю статистику
    statistics = group.stats()

    # Вывожу основную статистику
    print(f"\n ОБЩАЯ СТАТИСТИКА:")
    print(f"   Всего студентов: {statistics['count']}")
    print(f"   Минимальный GPA: {statistics['min_gpa']:.2f}")
    print(f"   Максимальный GPA: {statistics['max_gpa']:.2f}")
    print(f"   Средний GPA: {statistics['avg_gpa']:.2f}")

    print(f"\n РАСПРЕДЕЛЕНИЕ ПО ГРУППАМ:")
    for group_name, count in statistics['groups'].items():
        percentage = (count / statistics['count']) * 100
        print(f"   {group_name}: {count} студентов ({percentage:.1f}%)")

    print(f"\n ТОП-5 СТУДЕНТОВ:")
    for i, student in enumerate(statistics['top_5_students'], 1):
        print(f"   {i}. {student['fio']} - GPA: {student['gpa']:.2f}")

    # Вывожу дополнительную статистику
    print(f"\n ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА:")
    print(f"   Медианный GPA: {statistics['median_gpa']:.2f}")
    print(f"   Стандартное отклонение GPA: {statistics['std_dev_gpa']:.2f}")
    print(f"   Разброс GPA: {statistics['gpa_range']:.2f}")
    print(f"   Самая многочисленная группа: {statistics['most_common_group']}")
    print(f"   Студентов в ней: {statistics['students_in_most_common_group']}")

    # Пример аналитики на основе статистики
    print(f"\n АНАЛИТИКА:")
    if statistics['std_dev_gpa'] < 0.5:
        print("   GPA студентов распределен равномерно")
    else:
        print("   Есть значительный разброс в успеваемости студентов")

    if statistics['avg_gpa'] > 4.0:
        print("   Средний уровень успеваемости высокий")
    elif statistics['avg_gpa'] > 3.0:
        print("   Средний уровень успеваемости удовлетворительный")
    else:
        print("   Средний уровень успеваемости низкий")

    # Визуализация распределения GPA (текстовая)
    print(f"\n ГИСТОГРАММА GPA (грубо):")
    gpa_ranges = {
        "5.0": 0,
        "4.0-4.9": 0,
        "3.0-3.9": 0,
        "2.0-2.9": 0,
        "0.0-1.9": 0
    }

    students = group.list()
    for student in students:
        gpa = student.gpa
        if gpa == 5.0:
            gpa_ranges["5.0"] += 1
        elif gpa >= 4.0:
            gpa_ranges["4.0-4.9"] += 1
        elif gpa >= 3.0:
            gpa_ranges["3.0-3.9"] += 1
        elif gpa >= 2.0:
            gpa_ranges["2.0-2.9"] += 1
        else:
            gpa_ranges["0.0-1.9"] += 1

    for range_name, count in gpa_ranges.items():
        bar = "█" * count
        print(f"   {range_name:8} | {bar} ({count})")

    print("=" * 60)

    # Удаляю тестовый файл
    os.remove(test_file)


# Пример использования в основном коде
if __name__ == "__main__":
    demonstrate_stats()

    # Пример интеграции в существующий код
    print("\n\nПример использования в основном классе:")

    # Создаю реальный файл
    group = Group("../../data/lab09/students_stats.csv")

    # Добавляю несколько студентов
    group.add(Student("Иванов Иван", "2000-01-01", "БИВТ-21-1", "4.5"))
    group.add(Student("Петров Петр", "2000-02-02", "БИВТ-21-2", "3.8"))
    group.add(Student("Сидоров Сидор", "2000-03-03", "БИВТ-21-1", "4.2"))

    # Получаю статистику
    stats = group.stats()
    print(f"\nСтатистика по группе:")
    print(f"Количество: {stats['count']}")
    print(f"Средний GPA: {stats['avg_gpa']:.2f}")
    print(f"Распределение по группам: {stats['groups']}")