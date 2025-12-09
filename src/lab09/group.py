import csv
import os
from datetime import datetime
from typing import List, Optional, Dict, Any


class Student:
    """Вспомогательный класс для представления студента"""

    def __init__(self, fio: str, birthdate: str, group: str, gpa: str):
        self.fio = fio
        self.birthdate = birthdate
        self.group = group
        self.gpa = gpa

    def __repr__(self):
        return f"Student(fio='{self.fio}', birthdate='{self.birthdate}', group='{self.group}', gpa='{self.gpa}')"

    def to_dict(self) -> Dict[str, str]:
        """Конвертирует объект Student в словарь"""
        return {
            'fio': self.fio,
            'birthdate': self.birthdate,
            'group': self.group,
            'gpa': self.gpa
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
        """
        Создает файл с заголовком, если его ещё нет

        Создает CSV файл с заголовками, если файл не существует.
        Если файл существует, проверяет корректность заголовков.
        """
        # Если файл не существует, создаю его с заголовком
        if not os.path.exists(self.path):
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.HEADER)
                writer.writeheader()
        else:
            # Проверяю существующий файл на наличие корректного заголовка
            try:
                with open(self.path, 'r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    if reader.fieldnames != self.HEADER:
                        raise ValueError(
                            f"Неверный формат CSV файла. Ожидаемые заголовки: {self.HEADER}, "
                            f"полученные: {reader.fieldnames}"
                        )
            except csv.Error as e:
                raise ValueError(f"Ошибка чтения CSV файла: {e}")

    def _read_all(self) -> List[Dict[str, str]]:
        """
        Читает все строки из CSV и возвращает список словарей

        Returns:
            Список словарей, где каждый словарь представляет студента

        Raises:
            ValueError: если строка содержит неверное количество полей
        """
        students = []
        with open(self.path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Проверка заголовка
            if reader.fieldnames != self.HEADER:
                raise ValueError(f"Неверный формат заголовка CSV файла")

            for i, row in enumerate(reader, start=2):  # start=2 для учета заголовка
                # Проверяю, что все поля присутствуют
                if len(row) != len(self.HEADER):
                    raise ValueError(
                        f"Строка {i}: неверное количество полей. "
                        f"Ожидалось {len(self.HEADER)}, получено {len(row)}"
                    )

                # Проверяю, что все поля заполнены
                for field in self.HEADER:
                    if field not in row or row[field] is None:
                        raise ValueError(f"Строка {i}: отсутствует поле '{field}'")

                students.append(row)

        return students

    def list(self) -> List[Student]:
        """
        Возвращает всех студентов в виде списка объектов Student

        Returns:
            Список объектов Student

        Raises:
            ValueError: если данные в CSV некорректны
        """
        students_data = self._read_all()
        students = []

        for data in students_data:
            # Валидация данных при создании объекта Student
            try:
                # Проверяю GPA (должно быть числом)
                gpa = data['gpa']
                if not self._is_valid_gpa(gpa):
                    raise ValueError(f"Некорректное значение GPA: {gpa}")

                student = Student(
                    fio=data['fio'],
                    birthdate=data['birthdate'],
                    group=data['group'],
                    gpa=gpa
                )
                students.append(student)
            except Exception as e:
                raise ValueError(f"Ошибка при создании студента из данных {data}: {e}")

        return students

    def add(self, student: Student) -> None:
        """
        Добавляет нового студента в CSV файл

        Args:
            student: объект Student для добавления

        Raises:
            ValueError: если студент с таким ФИО уже существует
        """
        # Проверяю валидность GPA
        if not self._is_valid_gpa(student.gpa):
            raise ValueError(f"Некорректное значение GPA: {student.gpa}")

        # Проверяю, нет ли уже студента с таким ФИО
        existing_students = self.list()
        for existing in existing_students:
            if existing.fio == student.fio:
                raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")

        # Добавляю студента в файл
        with open(self.path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.HEADER)
            writer.writerow(student.to_dict())

    def find(self, substr: str) -> List[Student]:
        """
        Находит студентов по подстроке в ФИО

        Args:
            substr: подстрока для поиска в поле fio

        Returns:
            Список объектов Student, у которых в ФИО содержится substr
        """
        all_students = self.list()
        result = []

        # Поиск без учета регистра
        substr_lower = substr.lower()
        for student in all_students:
            if substr_lower in student.fio.lower():
                result.append(student)

        return result

    def remove(self, fio: str) -> int:
        """
        Удаляет запись(и) с данным ФИО

        Args:
            fio: полное ФИО для удаления

        Returns:
            Количество удаленных записей
        """
        all_students = self.list()
        # Оставляю только студентов, у которых ФИО не совпадает с искомым
        students_to_keep = [s for s in all_students if s.fio != fio]
        removed_count = len(all_students) - len(students_to_keep)

        if removed_count > 0:
            # Перезаписываю файл с оставшимися студентами
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.HEADER)
                writer.writeheader()
                for student in students_to_keep:
                    writer.writerow(student.to_dict())

        return removed_count

    def update(self, fio: str, **fields: Any) -> int:
        """
        Обновляет поля существующего студента

        Args:
            fio: ФИО студента для обновления
            **fields: поля для обновления (ключ-значение)

        Returns:
            Количество обновленных записей

        Raises:
            ValueError: если переданы некорректные поля
        """
        # Проверяю, что все передаваемые поля допустимы
        for field in fields.keys():
            if field not in self.HEADER:
                raise ValueError(f"Недопустимое поле: '{field}'. Допустимые поля: {self.HEADER}")

        # Проверяю валидность GPA, если оно передано
        if 'gpa' in fields and not self._is_valid_gpa(str(fields['gpa'])):
            raise ValueError(f"Некорректное значение GPA: {fields['gpa']}")

        all_students = self.list()
        updated_count = 0

        # Обновляю студентов с заданным ФИО
        for student in all_students:
            if student.fio == fio:
                updated_count += 1
                for field, value in fields.items():
                    setattr(student, field, str(value))

        if updated_count > 0:
            # Перезаписываю файл с обновленными данными
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.HEADER)
                writer.writeheader()
                for student in all_students:
                    writer.writerow(student.to_dict())

        return updated_count

    def _is_valid_gpa(self, gpa_str: str) -> bool:
        """
        Проверяет валидность GPA

        Args:
            gpa_str: строка с GPA

        Returns:
            True если GPA валидно, иначе False
        """
        try:
            gpa = float(gpa_str)
            return 0.0 <= gpa <= 5.0  # Предполагаю 5-балльную систему
        except (ValueError, TypeError):
            return False


# Пример использования
if __name__ == "__main__":
    # Создаю группу (файл будет создан автоматически)
    group = Group("students.csv")

    # Добавляю студентов
    student1 = Student("Иванов Иван Иванович", "2000-05-15", "Группа 101", "4.5")
    student2 = Student("Петров Петр Петрович", "2001-03-20", "Группа 101", "3.8")

    try:
        group.add(student1)
        group.add(student2)
    except ValueError as e:
        print(f"Ошибка при добавлении: {e}")

    # Вывожу всех студентов
    print("Все студенты:")
    for student in group.list():
        print(f"  {student}")

    # Ищу студентов по подстроке
    print("\nПоиск 'Иванов':")
    for student in group.find("Иванов"):
        print(f"  {student}")

    # Обновляю данные студента
    print(f"\nОбновляем студента {student1.fio}:")
    updated = group.update(student1.fio, gpa="4.8", group="Группа 102")
    print(f"  Обновлено записей: {updated}")

    # Проверяю обновление
    print("\nПосле обновления:")
    for student in group.list():
        print(f"  {student}")

    # Удаляю студента
    print(f"\nУдаляем студента {student2.fio}:")
    removed = group.remove(student2.fio)
    print(f"  Удалено записей: {removed}")

    print("\nОставшиеся студенты:")
    for student in group.list():
        print(f"  {student}")