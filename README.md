# python_labs1
## Лабораторная работа №1
## Задание №1
Программа для приветствия пользователя и расчета возраста через год.

Что делает:
- Запрашивает имя пользователя
- Запрашивает текущий возраст
- Вычисляет возраст через год
- Выводит персональное приветствие с будущим возрастом
  
```python
# Получаю имя, удаляю лишние пробелы
name = input("Имя: ").strip()
# Получаю возраст, удаляю пробелы, преобразую в число
age = int(input("Возраст: ").strip())
# Вывожу приветствие с вычислением возраста через год
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```

### Описание программы
Эта программа на Python запрашивает у пользователя его имя и возраст, потом вычисляет возраст пользователя через год и сообщение-приветствие.

### Пример выполнения

<img width="1920" height="1200" alt="image01_Kolesnichenko Daria" src="https://github.com/user-attachments/assets/2af32bf5-224a-406f-b7eb-b78936f70326" />



## Задание №2
Программа для вычисления суммы и среднего арифметического двух чисел.

Что делает:
- Принимает два числа (поддерживает и точку, и запятую как разделитель)
- Вычисляет их сумму
- Вычисляет среднее арифметическое
- Выводит результаты с точностью до двух знаков после запятой
  
```python
# Исходные данные (строки с запятыми)
a = "3,5"
b = "4,25"
# Вывод исходных значений
print(f"a={a},b = {b}")
# Преобразование в числа
a = float(a.replace(',', '.'))
b = float(b.replace(',', '.'))
# Математические операции
sum_result = a + b
avg_result = sum_result / 2
# Вывод результатов с округлением до 2 знаков
print(f"sum={sum_result:.2f}; avg={avg_result:.2f}")
```
### Описание программы
Эта программа на Python запрашивает у пользователя два действительных числа, вычисляет их сумму и среднее арифметическое, потом выводит результат.

### Пример выполнения

<img width="1920" height="1200" alt="img02 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/9461057f-a291-4fc2-9e0f-b1ef15821ac6" />

## Задание №3
Программа для расчета итоговой стоимости товара со скидкой и НДС.

Что делает:
- Принимает исходную цену товара
- Принимает процент скидки
- Принимает процент НДС (налог на добавленную стоимость)
- Рассчитывает:
  1. Цену после применения скидки
  2. Сумму НДС от цены со скидкой
  3. Итоговую стоимость к оплате
- Выводит все значения в формате чека с выравниванием
  
```python
# Ввод и очистка данных от пользователя
price = input("Введите цену: ").strip().replace(',', ".")
discount = input("Введите скидку: ").strip().replace(',', '.')
vat = input("Введите НДС: ").strip().replace(',', '.')
# Преобразование в числа
price = float(price)
discount = float(discount)
vat = float(vat)
# Расчеты
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
# Вывод результатов
print(f"База после скидки: {base:.2f}")
print(f"НДС: {vat_amount:.2f}")
print(f"Итого к оплате: {total:.2f}")
```
### Описание программы
Эта программа на Python запрашивает у пользователя цену товара, размер скидки и НДС, потом вычисляет стоимость с учётом скидки, сумму налога и итоговую сумму к оплате.

### Пример выполнения 

<img width="1920" height="1200" alt="img03_Kolesnichenko Daria" src="https://github.com/user-attachments/assets/804d8d9b-397b-4db1-9fc5-c504e2e4fd33" />


## Задание №4
Программа для преобразования минут в формат ЧЧ:ММ.

Что делает:
- Принимает количество минут (целое число)
- Переводит минуты в часы и минуты
- Выводит результат в формате ЧЧ:ММ, где минуты всегда двузначные
  
```python
# Получаю общее количество минут от пользователя
m = int(input("Минуты: "))
# Вычисляю часы (целая часть от деления на 60)
hours = m // 60
# Вычисляю оставшиеся минуты (остаток от деления на 60)
minutes = m % 60
# Вывожу результат в формате ЧЧ:ММ
print(f"{hours}:{minutes:02d}")
```
### Описание программы
Эта программа на Python запрашивает у пользователя количество минут, затем преобразует их в формат часов и минут.

### Пример выполнения

<img width="1920" height="1200" alt="img04_Kolesnichenko Daria" src="https://github.com/user-attachments/assets/34fe5d2b-ca88-46f1-978c-1be0d2ebc148" />


## Задаине №5
Программа для обработки ФИО: получения инициалов и подсчета длины.

Что делает:
- Принимает ФИО (может быть с лишними пробелами)
- Убирает лишние пробелы между словами
- Формирует инициалы из первых букв каждого слова
- Подсчитывает длину очищенной строки ФИО
- Выводит инициалы и длину строки
  
```python
# Получаю ФИО от пользователя
fio_input = input("ФИО: ")
# Удаляю лишние пробелы в начале и конце
fio_cleaned = fio_input.strip()
# Разбиваю на отдельные слова
words = fio_cleaned.split()
# Создаю инициалы: берю первую букву каждого слова и делаю заглавной
initials = ''.join(word[0].upper() for word in words if word)
# Вывожу результаты
print(f"Инициалы: {initials}.")
print(f"Длина символов: {len(fio_cleaned)}")
```
### Описание программы
Эта программа на Python запрашивает у пользователя ФИО,выбирает инициалы и считает общую длину строки(количество символов), включая ФИО.

### Пример выполнения

<img width="1920" height="1200" alt="img05_Kolesnichenko Daria" src="https://github.com/user-attachments/assets/ef90e54b-30cc-4abc-9928-6a328f940d0a" />


## Вывод
В процессе лабораторной работы я изучила базовые принципы программирования на языке Python. Освоила работу с пользовательским вводом, выполнение математических операций, обработку текстовых данных и форматирование вывода. Также я научилась использовать GitHub для управления версиями кода и ведения проектов.














## Лабораторная работа №2
## Задание №1
Программа находит минимальное и максимальное значение в списке чисел.
Эта функция принимает список чисел и возвращает кортеж из двух элементов: первый элемент - наименьшее число в списке, второй элемент - наибольшее число.
Args:
    nums (list): Список чисел (целых или дробных), которые нужно проверить
        
Returns:
    tuple: Кортеж в формате (минимальное_значение, максимальное_значение)
        
Raises:
    ValueError: Если передан пустой список (нельзя найти min/max в пустом списке)
    
```python
# Объявление функции с аннотацией типов
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
# Проверка на пустой список
    if len(nums) == 0:
 # Если список пустой - вызываю ошибку
        raise ValueError("Список не может быть пустым")
    else:
# Возвращаю кортеж (минимальный элемент, максимальный элемент)
        return min(nums), max(nums)
# Тестирование функции с разными входными данными
# Список целых чисел с повторениями
print(min_max([3, -1, 5, 5, 0]))
# Список с одним элементом
print(min_max([42]))
# Список смешанных типов (float и int)
print(min_max([1.5, 2, 2.0, -3.1]))
# Список отрицательных чисел
print(min_max([-5, -2, -9]))
# Пустой список (вызовет ошибку)
print(min_max([]))
```
### Описание программы
Эта программа на Python находит максимальный и минимальный элмент в списке чисел.Если список пустой, возвращает ошибку.
Принцип работы:
- Если список содержит несколько одинаковых минимальных/максимальных значений, функция вернет это значение для обеих позиций.
- Для списка из одного элемента вернет этот элемент как минимум и как максимум.
- Работает с любыми числами: целыми, дробными, отрицательными, положительными.
- Не изменяет исходный список.


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-06_20-05-00" src="https://github.com/user-attachments/assets/fe2c8645-e636-413a-b2cc-d95a32543260" />

Программа удаляет повторяющиеся числа из списка и сортирует оставшиеся по возрастанию.
Эта функция выполняет две операции сразу:
 1. Убирает все дубликаты (оставляет только уникальные числа)
 2. Сортирует полученные числа от меньшего к большему
Args:
    nums (list): Список чисел (целых или дробных), которые нужно обработать
Returns:
    list: Новый список с уникальными числами, отсортированными по возрастанию
    
```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
# Преобразую список в множество (удаляю дубликаты), затем сортирую
    return sorted(set(nums))
# Тестирование функции
print(sorted(set([3, 1, 2, 1, 3])))
print(sorted(set([])))
print(sorted(set([-1, -1, 0, 2, 2])))
print(sorted(set([1.0, 1, 2.5, 2.5, 0])))
```
### Описание программы
Эта программа на Python возвращает отсортированный список уникальных элементов из входного списка.
Принцип работы:
- set(nums) - создает множество из списка, автоматически удаляя все дубликаты
- sorted() - сортирует элементы множества по возрастанию
- Возвращает новый список, исходный список не изменяется.


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-06_20-31-06" src="https://github.com/user-attachments/assets/c0b9d0f4-9bc9-4e49-8538-5e00c7b6d7de" />


Программа преобразует список списков или кортежей в один плоский список.
Эта функция "разворачивает" вложенные структуры, собирая все элементы из внутренних списков и кортежей в один общий список.
Args:
     mat (list): Список, содержащий списки или кортежи с элементами
Returns:
    list: Одномерный список со всеми элементами из вложенных структур
Raises:
    TypeError: Если какой-то элемент входного списка не является списком или кортежем.
    
```python
def flatten(mat: list[list | tuple]) -> list:
# Создаю пустой список для результатов
    result = []
# Перебираю каждый элемент во входном списке
    for obj in mat:
# Проверяю тип элемента
        if not isinstance(obj, (list, tuple)):
# Если элемент не список и не кортеж - ошибка
            raise TypeError(f"Элемент {obj} не является списком или кортежем")
        else:
# Если элемент правильный - перебираю его содержимое
            for item in obj:
                result.append(item)
# Возвращаю "выровненный" список
    return result
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], 'ab']))
print(flatten([1, 2],(3, 4, 5)))
```

### Описание программы
Эта программа на Python преобразует список списков или кортежей в одномерный список.
Принцип работы:
- Проходит по каждому элементу входного списка.
- Проверяет, что элемент является списком или кортежем.
- Добавляет все элементы из этого списка/кортежа в результат.
- Пустые списки/кортежи просто игнорируются (ничего не добавляют).


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-06_20-42-16" src="https://github.com/user-attachments/assets/e8ff9b10-4dc7-47db-a54c-2fbba97fe4d0" />


## Задание B
Программа транспонирует матрицу (меняет строки и столбцы местами).
Эта функция преобразует матрицу таким образом, что:
- первая строка становится первым столбцом
- вторая строка становится вторым столбцом
- и так далее...
Другими словами, элемент на позиции [i][j] в исходной матрице окажется на позиции [j][i] в результирующей матрице.
Args:
    mat (list): Двумерный список (матрица) чисел
Returns:
          list: Транспонированная матрица
Raises:
    ValueError: Если строки матрицы имеют разную длину
                   (матрица не прямоугольная)
  
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
 # Проверка на пустую матрицу
    if len(mat) == 0:
        return []
# Запоминаю длину первой строки как эталон
    rowlenght = len(mat[0])
# Проверяю, что все строки одинаковой длины
    for row in mat:
        if len(row) != rowlenght:
            raise ValueError
# Транспонирование: превращаю столбцы в строки
    return [[row[index] for row in mat] for index in range(rowlenght)]
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([[]]))
print(transpose([[1, 2], [3]]))
```

### Описание программы
Данная программа реализует функцию transpose(), которая выполняет транспонирование матрицы - операцию, при которой строки матрицы становятся столбцами, а столбцы - строками.
Принцип работы:
- Сначала проверяет, что все строки имеют одинаковую длину.
- Затем создает новую матрицу, где берет элементы с одинаковыми индексами из каждой строки и формирует из них новые строки.


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-06_22-40-21" src="https://github.com/user-attachments/assets/d982a33d-8330-4d24-89fe-99eb32793145" />

Программа вычисляет сумму элементов каждой строки в матрице.
Эта функция проходит по всем строкам матрицы и для каждой строки вычисляет сумму всех чисел в этой строке.
Args:
    mat (list): Двумерный список (матрица) чисел
Returns:
          list: Список сумм каждой строки, в том же порядке, что и строки
Raises:
    ValueError: Если строки матрицы имеют разную длину
                   (матрица не прямоугольная)
                   
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
 # Проверка на пустую матрицу
    if len(mat) == 0:
        return []
# Запоминаем длину первой строки как эталон
    rowlenght = len(mat[0])
 # Проверяем, что все строки одинаковой длины
    for row in mat:
        if len(row) != rowlenght:
            raise ValueError
 # Вычисляем сумму для каждой строки
    return [sum(row) for row in mat]
# Тестирование функции
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
```


### Описание программы
Эта программа на Python вычисляет суммы элементов каждой строки в матрице (двумерном списке).
Принцип работы:
- Сначала проверяет, что все строки имеют одинаковую длину.
- Затем для каждой строки вычисляет сумму всех её элементов.
- Возвращает список этих сумм.


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-06_22-53-53" src="https://github.com/user-attachments/assets/3dc1365c-8efc-4420-b73a-27210bccb772" />



Программа транспонирует матрицу (меняет строки и столбцы местами)...
Args:
     mat (list): Двумерный список (матрица) чисел
Returns:
           list: Транспонированная матрица
           
и вычисляет сумму элементов каждого столбца в матрице.
Эта функция находит сумму всех чисел в каждом столбце матрицы и возвращает список этих сумм в порядке столбцов.
Args:
      mat (list): Двумерный список (матрица) чисел
Returns:
            list: Список сумм каждого столбца
Raises:
      ValueError: Если строки матрицы имеют разную длину
                   (матрица не прямоугольная)
                   
```python
def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    if len(mat) == 0:
        return []
# Транспонирование: столбцы становятся строками
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

def col_sums(mat: list[list[float | int]]) -> list[float]:
# Проверка, что матрица прямоугольная
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")
# Транспонируем и вычисляем суммы строк (бывших столбцов)
    newmat = transpose(mat)
    return [sum(row) for row in newmat]
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```


### Описание программы
Эта программа на Python вычисляет суммы столбцов матрицы.
Принцип работы:
1. Сначала проверяет, что все строки имеют одинаковую длину.
2. Транспонирует матрицу (превращает столбцы в строки).
3. Вычисляет сумму каждой новой "строки" (которая была столбцом).


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-07_07-33-18" src="https://github.com/user-attachments/assets/ecca3f04-2069-4b28-98e0-5d9b3a9fd57b" />



## Задание С
Программа форматирует запись о студенте в единый стандартный вид.
Эта функция принимает кортеж с информацией о студенте и преобразует его в аккуратно отформатированную строку с правильным оформлением ФИО, группы и среднего балла.
Args:
    rec (tuple): Кортеж из трех элементов:
                 - ФИО (строка)
                 - группа (строка) 
                 - GPA (число - средний балл)
Returns:
        str: Отформатированная строка в формате: "Фамилия И.О., гр. ГРУППА, GPA ЧИСЛО"
Raises:
        ValueError: Если запись содержит не 3 элемента, если группа пустая, или если в ФИО меньше 2 частей.
        TypeError: Если GPA не является числом.
        
```python
def format_record(rec: tuple[str, str, float]) -> str:
# Проверка количества элементов
    if len(rec) != 3:
        raise ValueError("Запись должна содержать 3 элемента: ФИО, группа и GPA")
# Проверка типа GPA
    if not isinstance(rec[2], (int, float)):
        raise TypeError("GPA должен быть числом")
 # Проверка, что группа не пустая
    if len(rec[1].strip()) == 0:
        raise ValueError("Группа не может быть пустой")
# Обработка ФИО
    name_parts = rec[0].strip().split()
    if len(name_parts) < 2:
        raise ValueError("ФИО должно содержать фамилию и хотя бы одно имя")
# Форматируем фамилию
    surname = name_parts[0].capitalize()
# Создаем инициалы из остальных частей ФИО
    initials = '.'.join(name[0].upper() for name in name_parts[1:]) + '.'
# Форматируем итоговую строку
    return f"{surname} {initials}, гр. {rec[1]}, GPA {rec[2]:.2f}"
print(format_record(["Иванов Иван Иванович", "BIVT-25", 4.6]))
print(format_record(["Петров Пётр", "IKBO-12", 5.0]))
print(format_record(["  сидорова  анна   сергеевна ", "ABB-01", 3.999]))

```

### Описание программы
Эта программа на Python предназначена для форматирования записей о студентах в единый стандартизированный вид.
Принцип работы:
 1. Проверяет, что запись содержит ровно 3 элемента.
 2. Проверяет, что GPA - число.
 3. Проверяет, что группа не пустая.
 4. Разбирает ФИО: фамилия становится с заглавной буквы, имена преобразуются в инициалы с точками.
 5. Форматирует GPA с двумя знаками после запятой.
 6. Собирает всё в единую строку.


### Пример выполнения
<img width="1920" height="1200" alt="ex C Kolesnichenko Daria" src="https://github.com/user-attachments/assets/aa4d5847-1625-4563-ad47-279230bbaa70" />

## Вывод
Освоила операции над списками, кортежами, множествами и словарями. Научилась работать с 2D-списками (матрицами) — транспонирование, суммы по строкам/столбцам; аккуратно форматировать текстовые представления записей (на примере студента).
















## Лабораторная работа №3
## Задание A
```python
import re
from typing import List, Dict, Tuple


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""

    normalized = text

    if casefold:
        normalized = normalized.casefold()

    if yo2e:
        if casefold:
            normalized = normalized.replace('ё', 'е')
        else:
            normalized = normalized.replace('ё', 'е').replace('Ё', 'Е')

    normalized = re.sub(r'\s+', ' ', normalized)

    return normalized.strip()


def tokenize(text: str) -> List[str]:
    if not text:
        return []

    tokens = re.findall(r'\b\w+(?:-\w+)*\b', text, re.UNICODE)

    return tokens


def count_freq(tokens: List[str]) -> Dict[str, int]:

    freq_dict = {}

    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1

    return freq_dict


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    if not freq:
        return []

    sorted_items = sorted(
        freq.items(),

        key=lambda x: (-x[1], x[0]))

    return sorted_items[:n]
print(repr(normalize("ПрИвЕт\nМИр\t")))
print(repr(normalize("ёжик, Ёлка", yo2e=True)))
print(repr(normalize("Hello\r\nWorld")))
print(repr(normalize("  двойные   пробелы  ")))

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

tokens1 = ["a","b","a","c","b","a"]
freq1 = count_freq(tokens1)
print(freq1)
print(top_n(freq1, 2))

tokens2 = ["bb","aa","bb","aa","cc"]
freq2 = count_freq(tokens2)
print(freq2)
print(top_n(freq2, 2))
```

### Описание программы
Эта программа представляет собой набор утилит для обработки и анализа текста на Python: функция "normalize(text, casefold=True, yo2e=True)" нормализует текст: приводит к нижнему регистру (по умолчанию), заменяет букву "ё" на "е" (по умолчанию), убирает лишние пробелы и символы переноса; "tokenize(text)" разбивает текст на токены (слова): использует слова, включая дефисные конструкции, игнорирует знаки препинания и эмодзи; "count_freq(tokens)" подсчитывает частоту слов: создает словарь {слово: количество_вхождений}; "top_n(freq, n=5)" возвращает N самых частых слов: сортирует по убыванию частоты, при равной частоте - по алфавиту.

### Пример выполнения
normalize:
<img width="1920" height="1200" alt="normalize Daria Kolesnichenko laba 03" src="https://github.com/user-attachments/assets/3741e564-d90d-4c4d-9cd7-8d8d644c382e" />

tokenize:
<img width="1920" height="1200" alt="tokenize Daria Kolesnichenko laba 03" src="https://github.com/user-attachments/assets/84312860-931e-4aff-a7f7-28016d6d5138" />

count_freq + top_n:
<img width="1920" height="1200" alt="count_freq + top_n Daria Kolesnichenko laba 03" src="https://github.com/user-attachments/assets/e1f8acc8-c216-46a7-9f31-8b3e831fedf6" />


## Задание B
### Анализатор текста

### Использование

Скрипт читает **одну строку** текста из stdin.

#### Примеры запуска:

`powershell
# Через echo
echo "Текст для анализа" | python src\text_stats.py

# Через перенаправление ввода (одна строка в файле)
python src\text_stats.py < input.txt



```python
import sys
import re
from collections import Counter


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализация текста"""
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text = text.casefold()
    text = re.sub(r'[\t\r\n]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def tokenize(text: str) -> list[str]:
    """Разбивка на слова"""
    pattern = r'\b[\w-]+\b'
    tokens = re.findall(pattern, text)
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчет частоты"""
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Топ-N слов"""
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


def main():
    # Чтение одной строки
    text = sys.stdin.readline().strip()
    print(f"DEBUG: Получен текст: '{text}'")  # Отладочная информация

    if not text:
        print("Всего слов: 0")
        print("Уникальных слов: 0")
        print("Топ-5:")
        return

    normalized_text = normalize(text)
    print(f"DEBUG: После нормализации: '{normalized_text}'")

    tokens = tokenize(normalized_text)
    print(f"DEBUG: Токены: {tokens}")

    total_words = len(tokens)
    unique_words = len(set(tokens))
    freq_dict = count_freq(tokens)
    top_words = top_n(freq_dict, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
```

### Описание программы
Эта программа на Python анализирует текстовые данные, подсчитывает статистику слов и выводит наиболее часто встречающиеся слова. Она предназначена для обработки текста, введенного через стандартный ввод (stdin).


### Пример выполнения
<img width="1920" height="1200" alt="text_stats Kolesnichenko Daria laba 03" src="https://github.com/user-attachments/assets/3ed099f0-7b50-4169-9576-da767bfea0d6" />

## Вывод 
Нормализовала текст, аккуратно токенизировала, посчитала частоты слов и вывела топ-N.








## Лабораторная работа №4
## Задание A — модуль `src/lab04/io_txt_csv.py`
```python
import csv
from pathlib import Path
from typing import Union, List, Tuple


1. def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    """
    Читает содержимое текстового файла и возвращает его как одну строку.

    Args:
        path: Путь к файлу для чтения
        encoding: Кодировка файла. По умолчанию "utf-8".
                 Для русских текстов в Windows может потребоваться "cp1251"

    Returns:
        str: Содержимое файла как одна строка

    Raises:
        FileNotFoundError: Если файл не существует
        UnicodeDecodeError: Если не удается декодировать файл в указанной кодировке
    """
    path = Path(path)

    with open(path, 'r', encoding=encoding) as file:
        content = file.read()

    return content


2. def write_csv(rows: List[Union[Tuple, List]], path: Union[str, Path],
              header: Tuple[str, ...] = None) -> None:
    """
    Записывает данные в CSV файл с разделителем запятая.

    Args:
        rows: Список строк данных (каждая строка - tuple или list)
        path: Путь для сохранения CSV файла
        header: Опциональный заголовок для CSV файла

    Raises:
        ValueError: Если строки имеют разную длину
        OSError: Если невозможно записать файл
    """
    path = Path(path)

    ensure_parent_dir(path)

    if rows:
        first_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_length:
                raise ValueError(
                    f"Все строки должны иметь одинаковую длину. "
                    f"Строка {i} имеет длину {len(row)}, ожидается {first_length}. "
                    f"Строка: {row}"
                )

    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)


    def ensure_parent_dir(path: Union[str, Path]) -> None:
    """
    Создает родительские директории для указанного пути, если они не существуют.

    Args:
        path: Путь к файлу или директории
    """
    path = Path(path)
    parent_dir = path.parent

    if not parent_dir.exists():
        parent_dir.mkdir(parents=True, exist_ok=True)

### Мини-тесты
if __name__ == "__main__":
    print("=== Тестирование модуля io_txt_csv ===\n")

    try:
        # Подготовка тестовых данных
        test_dir = Path("test_data")
        test_dir.mkdir(exist_ok=True)

        print("1. Тестирование read_text():")

        # Создаем тестовые файлы
        (test_dir / "input.txt").write_text("Привет, мир!\nВторая строка.", encoding="utf-8")
        (test_dir / "empty.txt").write_text("", encoding="utf-8")

        # Тест чтения обычного файла
        content = read_text(test_dir / "input.txt")
        print(f"✓ input.txt: {repr(content)}")

        # Тест чтения пустого файла
        empty_content = read_text(test_dir / "empty.txt")
        print(f"✓ empty.txt: {repr(empty_content)}")

        print("\n2. Тестирование write_csv():")

        # Тест с данными и заголовком
        data = [("word", "count"), ("test", 3)]
        write_csv(data, test_dir / "check.csv")
        print("✓ check.csv создан")

        # Тест только с заголовком
        write_csv([], test_dir / "header_only.csv", header=("a", "b"))
        print("✓ header_only.csv создан")

        # Тест полностью пустого CSV
        write_csv([], test_dir / "empty.csv")
        print("✓ empty.csv создан")

        print("\n3. Тестирование ensure_parent_dir():")
        ensure_parent_dir(test_dir / "deep" / "nested" / "file.txt")
        print("✓ Родительские директории созданы")

        # Очистка
        import shutil

        shutil.rmtree(test_dir)
        if Path("deep").exists():
            shutil.rmtree("deep")

        print("\n✅ Все тесты пройдены успешно!")

    except Exception as e:
        print(f"❌ Ошибка при тестировании: {e}")
        raise
```
### Краевые случаи
```python
from src.lab04.io_txt_csv import read_text, write_csv
from pathlib import Path


def test_edge_cases():
    """Тестирование краевых случаев"""
    
    # Тест 1: Очень большой файл (имитация)
    print("1. Тест большого файла:")
    big_content = "x" * 10000  # 10KB текста
    Path("big_test.txt").write_text(big_content, encoding="utf-8")
    content = read_text("big_test.txt")
    print(f"✓ Большой файл прочитан, длина: {len(content)}")
    Path("big_test.txt").unlink()
    
    # Тест 2: CSV только с заголовком
    print("\n2. Тест CSV только с заголовком:")
    write_csv([], "header_only.csv", header=("name", "value"))
    header_content = Path("header_only.csv").read_text(encoding="utf-8")
    print(f"✓ Содержимое: {repr(header_content)}")
    Path("header_only.csv").unlink()
    
    # Тест 3: Полностью пустой CSV
    print("\n3. Тест полностью пустого CSV:")
    write_csv([], "completely_empty.csv")
    empty_size = Path("completely_empty.csv").stat().st_size
    print(f"✓ Размер пустого файла: {empty_size} байт")
    Path("completely_empty.csv").unlink()
    
    # Тест 4: Разная длина строк (должна быть ошибка)
    print("\n4. Тест разной длины строк:")
    try:
        invalid_data = [("a", "b"), ("c", "d", "e")]
        write_csv(invalid_data, "invalid.csv")
        print("❌ Ошибка: ValueError не был вызван")
    except ValueError as e:
        print(f"✓ Ожидаемая ошибка: {e}")
    
    print("\n✅ Все краевые случаи проверены!")


if __name__ == "__main__":
    test_edge_cases()
```
### Описание программы
Эта программа на Python представляет собой утилиту для работы с текстовыми и CSV-файлами. Вот подробное описание:
1. Функция read_text()
Назначение: Чтение содержимого текстового файла.
Параметры:
path - путь к файлу (строка или Path-объект);
encoding - кодировка файла (по умолчанию "utf-8").
Особенности:
Возвращает всё содержимое файла как одну строку.
Предусматривает работу с различными кодировками.
Автоматически обрабатывает путь с помощью Pathlib.
Имеет обработку исключений для отсутствующих файлов и проблем с кодировкой.
2. Функция write_csv()
Назначение: Запись данных в CSV-файл.
Параметры:
rows - список строк данных (кортежи или списки);
path - путь для сохранения файла;
header - опциональный заголовок столбцов;
Особенности:
Использует запятую как разделитель.
Проверяет согласованность длины строк данных.
Автоматически создает родительские директории.
Поддерживает запись заголовка.
3. Вспомогательная функция ensure_parent_dir()
Назначение: Создание родительских директорий.
Функциональность:
Рекурсивно создает все необходимые директории для указанного пути.
Использует parents=True для создания всей иерархии директорий.
Не создает дубликаты существующих директорий.
Общее назначение:
Программа предоставляет функции для чтения текстовых файлов и записи данных в CSV-формате с автоматическим созданием необходимых директорий.

### Пример выполнения
<img width="1920" height="1200" alt="io_text_csv Kolesnichenko Daria laba 04" src="https://github.com/user-attachments/assets/06876535-43dc-4682-a335-81f7357d68ae" />


## Задание B - скрипт`src/lab04/text_report.py`
```python
"""
Скрипт для анализа текста и генерации отчета частот слов.

Читает текстовый файл, анализирует частоты слов и создает CSV отчет.
"""

import sys
import argparse
from pathlib import Path
from collections import Counter

# Импорты из модулей проекта
try:
    from src.lab04.io_txt_csv import read_text, write_csv
    from src.lab03.text1 import normalize, tokenize
except ImportError:
    # Резервные импорты для случаев проблем с путями
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent))
    from src.lab04.io_txt_csv import read_text, write_csv
    from src.lab03.text1 import normalize, tokenize


def calculate_word_frequencies(text: str) -> dict[str, int]:
    """
    Вычисляет частоты слов в тексте.

    Args:
        text: Исходный текст для анализа

    Returns:
        Словарь {слово: частота}
    """
    if not text.strip():
        return {}

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    return Counter(tokens)


def get_top_words(freq: dict[str, int], n: int = None) -> list[tuple[str, int]]:
    """
    Возвращает слова, отсортированные по убыванию частоты.

    Args:
        freq: Словарь частот
        n: Количество слов для возврата (None = все слова)

    Returns:
        Список кортежей (слово, частота), отсортированных по частоте ↓, слову ↑
    """
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:n] if n is not None else sorted_words


def generate_report(input_file: Path, output_file: Path, encoding: str = "cp1251") -> bool:
    """
    Генерирует отчет по анализу текста.

    Args:
        input_file: Путь к входному файлу
        output_file: Путь для сохранения отчета
        encoding: Кодировка файла

    Returns:
        True если успешно, False при ошибке
    """
    try:
        # Чтение входного файла
        print(f"📖 Чтение файла: {input_file} (кодировка: {encoding})")
        text = read_text(input_file, encoding=encoding)

        # Анализ текста
        print("🔍 Анализ текста...")
        frequencies = calculate_word_frequencies(text)
        total_words = sum(frequencies.values())
        unique_words = len(frequencies)

        # Подготовка данных для CSV
        if frequencies:
            sorted_words = get_top_words(frequencies)
            write_csv(sorted_words, output_file, header=("word", "count"))
            print(f"💾 Отчет сохранен: {output_file}")
        else:
            # Пустой файл - создаем только заголовок
            write_csv([], output_file, header=("word", "count"))
            print("💾 Создан пустой отчет (только заголовок)")

        # Вывод статистики
        print("\n" + "=" * 40)
        print("📊 СТАТИСТИКА АНАЛИЗА ТЕКСТА")
        print("=" * 40)
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")

        if frequencies:
            top_5 = get_top_words(frequencies, 5)
            print("\n🏆 Топ-5 самых частых слов:")
            for i, (word, count) in enumerate(top_5, 1):
                print(f"  {i}. '{word}' - {count}")
        else:
            print("\n📭 Текст не содержит слов для анализа")
        print("=" * 40)

        return True

    except FileNotFoundError:
        print(f"❌ Ошибка: файл '{input_file}' не найден")
        return False
    except UnicodeDecodeError as e:
        print(f"❌ Ошибка кодировки: {e}")
        print("💡 Попробуйте указать другую кодировку: --encoding cp1251")
        return False
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return False


def main():
    """Основная функция скрипта."""
    parser = argparse.ArgumentParser(
        description="Анализ текста и генерация отчета частот слов",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  %(prog)s                                  # использует пути по умолчанию
  %(prog.py --in data/in.txt --out out.csv  # пользовательские пути
  %(prog)s --encoding cp1251               # для файлов из Windows
  %(prog)s -i text.txt -o report.csv -e windows-1251

Краевые случаи:
  • Если входной файл не существует - ошибка с кодом выхода 1
  • Если файл пустой - создается отчет только с заголовком
  • Проблемы с кодировкой - подсказка использовать --encoding
        """
    )

    parser.add_argument(
        '-i', '--in',
        dest='input_file',
        default='data/input.txt',
        help='Путь к входному текстовому файлу (по умолчанию: data/input.txt)'
    )

    parser.add_argument(
        '-o', '--out',
        dest='output_file',
        default='data/report.csv',
        help='Путь для сохранения CSV отчета (по умолчанию: data/report.csv)'
    )

    parser.add_argument(
        '-e', '--encoding',
        dest='encoding',
        default='utf-8',
        help='Кодировка входного файла (по умолчанию: utf-8). Для Windows файлов используйте cp1251'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Подробный вывод'
    )

    args = parser.parse_args()

    if args.verbose:
        print("🚀 Запуск анализа текста...")
        print(f"   Входной файл: {args.input_file}")
        print(f"   Выходной файл: {args.output_file}")
        print(f"   Кодировка: {args.encoding}")

    # Проверка и подготовка путей
    input_path = Path(args.input_file)
    output_path = Path(args.output_file)

    # Создание директории для выходного файла
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Запуск генерации отчета
    success = generate_report(input_path, output_path, args.encoding)

    if success:
        if args.verbose:
            print(f"✅ Задание выполнено успешно!")
        sys.exit(0)
    else:
        if args.verbose:
            print(f"❌ Задание завершено с ошибками")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
### Описание программы
Эта программа представляет собой скрипт для анализа текста и генерации отчета частот слов. Вот детальное описание:
Общее назначение:
Программа анализирует текстовый файл, подсчитывает частоту встречаемости слов и создает CSV-отчет с результатами.
Архитектура программы:
Основные компоненты:
1. Импорты и настройки.
Использует модули из предыдущих лабораторных работ (io_txt_csv, text1).
Имеет резервные импорты для решения проблем с путями.
Подключает argparse для обработки аргументов командной строки.
2. Функция calculate_word_frequencies(text)
Назначение: Подсчет частоты слов в тексте.
Процесс:
Нормализация текста (приведение к нижнему регистру).
Токенизация (разбиение на слова).
Подсчет частот с помощью Counter.
3. Функция get_top_words(freq, n)
Назначение: Сортировка слов по частоте.
Критерии сортировки:
По убыванию частоты (первичный).
По возрастанию слова (вторичный, при равных частотах).
4. Функция generate_report(input_file, output_file, encoding)
Назначение: Основная логика генерации отчета.
Процесс работы:
Чтение текстового файла.
Анализ частот слов.
Запись результатов в CSV.
Вывод статистики.

Обработка краевых случаев:
Пустые файлы (создается отчет только с заголовком).
Ошибки кодировки.
Отсутствующие файлы.
5. Функция main()
Назначение: Оркестрация работы программы.
Аргументы командной строки:
-i/--in - входной файл (по умолчанию: data/input.txt);
-o/--out - выходной файл (по умолчанию: data/report.csv);
-e/--encoding - кодировка файла (по умолчанию: utf-8);
-v/--verbose - подробный вывод.
### Пример выполнения
<img width="1920" height="1200" alt="text_report Kolesnichenko Daria laba 04" src="https://github.com/user-attachments/assets/0f10c27c-8b68-4c12-98ae-cb6fb838b76d" />

<img width="1920" height="1200" alt="text_report Kolesnichenko Daria laba 04 (2)" src="https://github.com/user-attachments/assets/c1342a74-13be-4ea4-b15e-d3a0c9951fa9" />

<img width="1920" height="1200" alt="text_report Kolesnichenko Daria laba 04(3)" src="https://github.com/user-attachments/assets/58d92ca9-8d9a-46e9-8542-3ab1cf2ecea5" />

### Тест-кейсы
```python
"""
Все тест-кейсы в одном скрипте без зависимостей.
"""

from pathlib import Path
import csv
import re
from collections import Counter


def process_test_case(test_name, input_text, expected_output):
    """Обрабатывает один тест-кейс"""
    print(f"\n{'=' * 60}")
    print(f"ТЕСТ-КЕЙС {test_name}")
    print(f"Вход: '{input_text}'")
    print('=' * 60)

    # Нормализация: casefold + ё→е
    normalized = input_text.lower().replace('ё', 'е')
    normalized = ' '.join(normalized.split())

    # Токенизация: \w+(?:-\w+)*
    tokens = re.findall(r'\w+(?:-\w+)*', normalized)

    # Подсчет частот
    freq = Counter(tokens)

    # Сортировка: count ↓, word ↑
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Сохранение CSV
    filename = f"data/report_{test_name.lower()}.csv"
    Path("data").mkdir(exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        if sorted_words:
            writer.writerows(sorted_words)

    # Вывод результатов
    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")

    if freq:
        print("Топ-5:")
        for word, count in sorted_words[:5]:
            print(f"{word}:{count}")
    else:
        print("Топ-5: нет данных")

    # Проверка ожидаемого результата
    print(f"\n✅ РЕЗУЛЬТАТ:")
    actual_output = dict(sorted_words)
    print(f"Получено: {actual_output}")
    print(f"Ожидалось: {expected_output}")

    if actual_output == expected_output:
        print("🎯 ТЕСТ ПРОЙДЕН!")
    else:
        print("❌ ТЕСТ НЕ ПРОЙДЕН!")

    # Показываем файл
    print(f"💾 Файл: {filename}")
    print(Path(filename).read_text(encoding="utf-8"))


def main():
    """Запуск всех тест-кейсов"""

    print("🎯 ЗАПУСК ТЕСТ-КЕЙСОВ ДЛЯ АНАЛИЗА ТЕКСТА")
    print("Создаю необходимые файлы...")

    # Тест-кейс A: Базовый случай
    process_test_case(
        "A",
        "Привет, мир! Привет!!!",
        {"привет": 2, "мир": 1}
    )

    # Тест-кейс B: Пустой файл
    process_test_case(
        "B",
        "",
        {}
    )

    # Тест-кейс C: Простой текст
    process_test_case(
        "C",
        "Привет",
        {"привет": 1}
    )

    


if __name__ == "__main__":
    main()
```
### Пример выполнения
<img width="1920" height="1200" alt="test-case Kolesnichenko Daria laba 04" src="https://github.com/user-attachments/assets/bc5c02df-2dab-4433-a246-1e62f851835c" />

<img width="1920" height="1200" alt="test-case Kolesnichenko Daria laba 04 (2)" src="https://github.com/user-attachments/assets/9663b2ea-b238-4e2e-b5a6-49113ea0afa0" />

## Вывод




































