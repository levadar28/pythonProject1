from collections import deque
from typing import Any, Optional


class Stack:
    def __init__(self):
        # внутреннее хранилище стека
        self._data = []

    def push(self, item):
        #  добавление в конец списка O(1)
        self._data.append(item)

    def pop(self):
        # добавлена обработка случая пустого стека
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        return self._data.pop()

    def peek(self):
        # при пустом стеке возвращаю None
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        # использую более питонический подход
        return not self._data

    def __len__(self) -> int:
        """Опционально: количество элементов в стеке."""
        return len(self._data)

    def __str__(self) -> str:
        """Строковое представление для отладки."""
        return f"Stack({self._data})"


class Queue:
    def __init__(self):
        # использую deque, как требуется в задании
        self._data = deque()

    def enqueue(self, item):
        # добавляю в конец очереди (справа)
        self._data.append(item)

    def dequeue(self):
        # удаляю с начала очереди (слева) и обрабатываю пустую очередь
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустой очереди")
        return self._data.popleft()

    def peek(self):
        # возвращает None при пустой очереди
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        # проверка на пустоту
        return not self._data

    def __len__(self) -> int:
        """Опционально: количество элементов в очереди."""
        return len(self._data)

    def __str__(self) -> str:
        """Строковое представление для отладки."""
        return f"Queue({list(self._data)})"


# Пример использования для тестирования
if __name__ == "__main__":
    print("Тестирование Stack:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Стек после push: {stack}")
    print(f"peek: {stack.peek()}")
    print(f"pop: {stack.pop()}")
    print(f"Стек после pop: {stack}")
    print(f"Длина стека: {len(stack)}")
    print(f"Пустой ли стек? {stack.is_empty()}")

    print("\nТестирование Queue:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Очередь после enqueue: {queue}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"Очередь после dequeue: {queue}")
    print(f"Длина очереди: {len(queue)}")
    print(f"Пустая ли очередь? {queue.is_empty()}")

    # Тестирование исключений
    print("\nТестирование исключений:")
    empty_stack = Stack()
    empty_queue = Queue()

    try:
        empty_stack.pop()
    except IndexError as e:
        print(f"Stack.pop() на пустом стеке: {e}")

    try:
        empty_queue.dequeue()
    except IndexError as e:
        print(f"Queue.dequeue() на пустой очереди: {e}")