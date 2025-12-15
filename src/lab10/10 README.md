Стек (Stack)
Принцип: LIFO (Last In, First Out) - последний вошёл, первый вышел
Аналогия из жизни: стопка тарелок, история браузера (кнопка "Назад")
Ключевые операции: push (добавить), pop (удалить), peek (посмотреть верхний)
Сложность операций: O(1) для всех основных операций

Очередь (Queue)
Принцип: FIFO (First In, First Out) - первый вошёл, первый вышел
Аналогия из жизни: очередь в магазине, очередь печати
Ключевые операции: enqueue (добавить в конец), dequeue (удалить из начала)
Сложность операций: O(1) для всех основных операций

Связный список (Linked List)

Принцип: цепочка узлов, каждый хранит данные и ссылку на следующий
Типы: односвязный, двусвязный, кольцевой
Аналогия: цепочка вагонов поезда
Преимущества: динамический размер, эффективная вставка/удаление
Недостатки: медленный доступ по индексу


Класс Stack
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        """Добавить элемент в стек"""
        self._items.append(item)
    
    def pop(self):
        """Удалить и вернуть верхний элемент"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """Посмотреть верхний элемент без удаления"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __len__(self):
        return len(self._items)

# Пример использования
stack = Stack()
stack.push(1)        # Стек: [1]
stack.push(2)        # Стек: [1, 2]
stack.push(3)        # Стек: [1, 2, 3]
print(stack.peek())  # 3
print(stack.pop())   # 3 (стек: [1, 2])
print(len(stack))    # 2


Класс Queue
from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        """Добавить элемент в очередь"""
        self._items.append(item)
    
    def dequeue(self):
        """Удалить и вернуть первый элемент"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()
    
    def front(self):
        """Посмотреть первый элемент без удаления"""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __len__(self):
        return len(self._items)

# Пример использования
queue = Queue()
queue.enqueue("Alice")   # Очередь: ["Alice"]
queue.enqueue("Bob")     # Очередь: ["Alice", "Bob"]
queue.enqueue("Charlie") # Очередь: ["Alice", "Bob", "Charlie"]
print(queue.front())     # "Alice"
print(queue.dequeue())   # "Alice" (очередь: ["Bob", "Charlie"])
print(len(queue))        # 2

Класс SinglyLinkedList
# Пример использования
lst = SinglyLinkedList()
lst.append(10)           # [10]
lst.append(20)           # [10, 20]
lst.prepend(5)           # [5, 10, 20]
lst.insert(2, 15)        # [5, 10, 15, 20]
lst.remove(10)           # [5, 15, 20]
print(lst)               # SinglyLinkedList([5, 15, 20])

# Итерация по списку
for item in lst:
    print(f"Элемент: {item}")

Бенчмарки и производительность
Тестирование производительности
import timeit
import random

def benchmark_operations():
    """Сравнение производительности разных структур"""
    
    sizes = [100, 1000, 10000]
    results = {}
    
    for size in sizes:
        print(f"\n{'='*50}")
        print(f"Размер данных: {size}")
        print('='*50)
        
        # Тестируем стек
        stack_setup = f"stack = Stack()"
        stack_stmt = f"""
for i in range({size}):
    stack.push(i)
for i in range({size}):
    stack.pop()
"""
        stack_time = timeit.timeit(stmt=stack_stmt, setup=stack_setup, globals=globals(), number=100)
        
        # Тестируем очередь
        queue_setup = f"queue = Queue()"
        queue_stmt = f"""
for i in range({size}):
    queue.enqueue(i)
for i in range({size}):
    queue.dequeue()
"""
        queue_time = timeit.timeit(stmt=queue_stmt, setup=queue_setup, globals=globals(), number=100)
        
        # Тестируем список
        list_setup = f"lst = SinglyLinkedList()"
        list_stmt = f"""
for i in range({size}):
    lst.append(i)
for i in range({size//2}):
    lst.prepend(i)
"""
        list_time = timeit.timeit(stmt=list_stmt, setup=list_setup, globals=globals(), number=100)
        
        print(f"Стек (push/pop {size} элементов): {stack_time:.6f} сек")
        print(f"Очередь (enqueue/dequeue {size} элементов): {queue_time:.6f} сек")
        print(f"Связный список (append/prepend): {list_time:.6f} сек")
        
        results[size] = {
            'stack': stack_time,
            'queue': queue_time,
            'linked_list': list_time
        }
    
    return results

# Запуск бенчмарка
benchmark_operations()

Почему связный список медленнее:
Выделение памяти:
Стек/Очередь: используют встроенные списки Python (list/deque).
Связный список: создаёт отдельные объекты Node для каждого элемента.
Результат: больше накладных расходов на создание объектов и сборку мусора.

Локальность данных:
Стек/Очередь: данные хранятся в непрерывном блоке памяти.
Связный список: данные разбросаны по разным участкам памяти.
Результат: кэш-промахи у связного списка, что замедляет доступ.

Внутренняя оптимизация Python:
list в Python оптимизирован на C-уровне
deque использует двусвязный список, но реализован на C
Реализация на Python медленнее из-за интерпретируемого кода.

Константные множители:
O(1) у связного списка имеет больший константный множитель.
Каждая операция требует создания объекта, установки ссылок, проверок.

Стек и очередь быстрее благодаря непрерывному хранению данных.
Связный список гибче, но имеет накладные расходы.
Выбор структуры зависит от конкретной задачи и операций.
Для большинства задач в Python встроенные структуры (list, deque) оптимальны.
Реализация структур на Python важна для обучения, но на практике используются встроенные оптимизированные версии.



