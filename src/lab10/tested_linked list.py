from src.lab10.linked_list import SinglyLinkedList


def test_singly_linked_list():
    print("=== Тестирование SinglyLinkedList ===")

    # Тест 1: Создание и базовые операции
    lst = SinglyLinkedList()
    print(f"Пустой список: {lst}")
    print(f"Длина пустого списка: {len(lst)}")

    # Тест 2: Добавление элементов
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(f"После добавления 1, 2, 3: {lst}")
    print(f"Длина: {len(lst)}")

    # Тест 3: Добавление в начало
    lst.prepend(0)
    print(f"После prepend(0): {lst}")

    # Тест 4: Вставка по индексу
    lst.insert(2, 1.5)
    print(f"После insert(2, 1.5): {lst}")

    # Тест 5: Итерация
    print("Элементы списка (итерация):")
    for item in lst:
        print(f"  - {item}")

    # Тест 6: Удаление по значению
    lst.remove(1.5)
    print(f"После remove(1.5): {lst}")

    # Тест 7: Удаление по индексу
    lst.remove_at(0)
    print(f"После remove_at(0): {lst}")

    # Тест 8: Проверка обработки ошибок
    try:
        lst.insert(100, 99)
    except IndexError as e:
        print(f"Ошибка при вставке по неверному индексу: {e}")

    # Тест 9: Сложные операции
    lst2 = SinglyLinkedList()
    for i in range(5):
        lst2.append(i * 10)
    print(f"\nВторой список: {lst2}")

    # Тест 10: Добавление в конец большого списка
    for i in range(3):
        lst2.append(50 + i)
    print(f"После добавления элементов в конец: {lst2}")
    print(f"Длина второго списка: {len(lst2)}")


if __name__ == "__main__":
    test_singly_linked_list()