from dataclasses import dataclass, fields
from datetime import date, datetime
import json
from typing import Dict, Any


@dataclass
class Student:
    fio: str
    birthdate: str  # формат YYYY-MM-DD
    group: str
    gpa: float

    def __post_init__(self):
        # Валидация даты рождения
        try:
            datetime.strptime(self.birthdate, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Неверный формат даты. Используйте YYYY-MM-DD")

        # Валидация среднего балла
        if not 0 <= self.gpa <= 5:
            raise ValueError("GPA должен быть в диапазоне от 0 до 5")

    def age(self) -> int:
        """Возвращает количество полных лет на текущую дату"""
        birth_date = datetime.strptime(self.birthdate, '%Y-%m-%d').date()
        today = date.today()

        # Вычисляю разницу в годах
        age_years = today.year - birth_date.year

        # Корректирую, если день рождения в этом году ещё не наступил
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1

        return age_years

    def to_dict(self) -> Dict[str, Any]:
        """Сериализация в словарь"""
        return {
            'fio': self.fio,
            'birthdate': self.birthdate,
            'group': self.group,
            'gpa': self.gpa
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student':
        """Десериализация из словаря"""
        # Фильтрую только нужные поля
        field_names = {f.name for f in fields(cls)}
        filtered_data = {k: v for k, v in data.items() if k in field_names}
        return cls(**filtered_data)

    def __str__(self) -> str:
        """Красивый строковый вывод"""
        return (f"Студент: {self.fio}\n"
                f"Дата рождения: {self.birthdate} (Возраст: {self.age()} лет)\n"
                f"Группа: {self.group}\n"
                f"Средний балл: {self.gpa:.2f}")


# Пример использования
if __name__ == "__main__":
    # Создание объекта
    student1 = Student(
        fio="Иванов Иван Иванович",
        birthdate="2000-05-15",
        group="SE-01",
        gpa=4.2
    )

    print("Объект студента:")
    print(student1)
    print()

    # Сериализация в словарь
    student_dict = student1.to_dict()
    print("Словарь:", student_dict)

    # Сериализация в JSON
    student_json = json.dumps(student_dict, ensure_ascii=False, indent=2)
    print("JSON:")
    print(student_json)
    print()

    # Десериализация из словаря
    student2 = Student.from_dict(student_dict)
    print("Восстановленный объект:")
    print(student2)
    print()

    # Проверка валидации
    try:
        Student(fio="Тест", birthdate="2020-20-20", group="SE-01", gpa=4.0)
    except ValueError as e:
        print(f"Ошибка валидации даты: {e}")

    try:
        Student(fio="Тест", birthdate="2000-01-01", group="SE-01", gpa=6.0)
    except ValueError as e:
        print(f"Ошибка валидации GPA: {e}")