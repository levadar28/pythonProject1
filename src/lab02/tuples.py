def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3:
        raise ValueError("Запись должна содержать 3 элемента: ФИО, группа и GPA")

    if not isinstance(rec[2], (int, float)):
        raise TypeError("GPA должен быть числом")

    if len(rec[1].strip()) == 0:
        raise ValueError("Группа не может быть пустой")

    name_parts = rec[0].strip().split()
    if len(name_parts) < 2:
        raise ValueError("ФИО должно содержать фамилию и хотя бы одно имя")

    surname = name_parts[0].capitalize()

    initials = '.'.join(name[0].upper() for name in name_parts[1:]) + '.'

    return f"{surname} {initials}, гр. {rec[1]}, GPA {rec[2]:.2f}"
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))