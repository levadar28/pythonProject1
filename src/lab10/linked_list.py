from typing import Any, Optional, Iterator


class Node:
    def __init__(self, value: Any, next: Optional['Node'] = None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0

    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка за O(1)"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка за O(1)"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:  # Список был пуст
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Вставить элемент по индексу"""
        if idx < 0 or idx > self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size}]")

        if idx == 0:
            self.prepend(value)
            return
        elif idx == self._size:
            self.append(value)
            return

        # Вставка в середину
        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def remove(self, value: Any) -> None:
        """Удалить первое вхождение значения из списка"""
        if self.head is None:
            return

        # Удаление головы
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            if self.head is None:  # Список стал пустым
                self.tail = None
            return

        # Поиск узла для удаления
        prev = self.head
        current = self.head.next

        while current is not None:
            if current.value == value:
                prev.next = current.next
                self._size -= 1
                # Если удалили хвост
                if current == self.tail:
                    self.tail = prev
                return
            prev = current
            current = current.next

    def remove_at(self, idx: int) -> None:
        """Удалить элемент по индексу"""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size - 1}]")

        if idx == 0:  # Удаление головы
            self.head = self.head.next
            if self.head is None:  # Список стал пустым
                self.tail = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next

            # current указывает на узел перед удаляемым
            current.next = current.next.next
            if current.next is None:  # Удалили хвост
                self.tail = current

        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        """Итератор по значениям списка"""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        """Количество элементов в списке"""
        return self._size

    def __repr__(self) -> str:
        """Строковое представление списка"""
        values = list(self)
        return f"SinglyLinkedList({values})"