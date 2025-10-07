# python_labs1
## Лабораторная работа №1
## Задание №1
```python
name = input("Имя: ").strip()
age = int(input("Возраст: ").strip())
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```

### Описание программы
Эта программа на Python запрашивает у пользователя его имя и возраст, потом вычисляет возраст пользователя через год и сообщение-приветствие.

### Пример выполнения

<img width="1920" height="1200" alt="image01_Kolesnichenko Daria" src="https://github.com/user-attachments/assets/2af32bf5-224a-406f-b7eb-b78936f70326" />



## Задание №2
```python
a = "3,5"
b = "4,25"
print(f"a={a},b = {b}")
a = float(a.replace(',', '.'))
b = float(b.replace(',', '.'))
sum_result = a + b
avg_result = sum_result / 2
print(f"sum={sum_result:.2f}; avg={avg_result:.2f}")
```
### Описание программы
Эта программа на Python запрашивает у пользователя два действительных числа, вычисляет их сумму и среднее арифметическое, потом выводит результат.

### Пример выполнения

<img width="1920" height="1200" alt="img02 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/9461057f-a291-4fc2-9e0f-b1ef15821ac6" />

## Задание №3
```python
price = input("Введите цену: ").strip().replace(',', ".")
discount = input("Введите скидку: ").strip().replace(',', '.')
vat = input("Введите НДС: ").strip().replace(',', '.')
price = float(price)
discount = float(discount)
vat = float(vat)
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f"База после скидки: {base:.2f}")
print(f"НДС: {vat_amount:.2f}")
print(f"Итого к оплате: {total:.2f}")
```
### Описание программы
Эта программа на Python запрашивает у пользователя цену товара, размер скидки и НДС, потом вычисляет стоимость с учётом скидки, сумму налога и итоговую сумму к оплате.

### Пример выполнения 

<img width="1920" height="1200" alt="img03_Kolesnichenko Daria" src="https://github.com/user-attachments/assets/804d8d9b-397b-4db1-9fc5-c504e2e4fd33" />


## Задание №4
```python
m = int(input("Минуты: "))
hours = m // 60
minutes = m % 60
print(f"{hours}:{minutes:02d}")
```
### Описание программы
Эта программа на Python запрашивает у пользователя количество минут, затем преобразует их в формат часов и минут.

### Пример выполнения

<img width="1920" height="1200" alt="img04_Kolesnichenko Daria" src="https://github.com/user-attachments/assets/34fe5d2b-ca88-46f1-978c-1be0d2ebc148" />


## Задаине №5
```python
fio_input = input("ФИО: ")
fio_cleaned = fio_input.strip()
words = fio_cleaned.split()
initials = ''.join(word[0].upper() for word in words if word)
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
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError("Список не может быть пустым")
    else:
        return min(nums), max(nums)
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([-5, -2, -9]))
print(min_max([]))
```
### Описание программы
Эта программа на Python находит максимальный и минимальный элмент в списке чисел.Если список пустой, возвращает ошибку.


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-06_20-05-00" src="https://github.com/user-attachments/assets/fe2c8645-e636-413a-b2cc-d95a32543260" />


```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
print(sorted(set([3, 1, 2, 1, 3])))
print(sorted(set([])))
print(sorted(set([-1, -1, 0, 2, 2])))
print(sorted(set([1.0, 1, 2.5, 2.5, 0])))
```
### Описание программы
Эта программа на Python возвращает отсортированный список уникальных элементов из входного списка.


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-06_20-31-06" src="https://github.com/user-attachments/assets/c0b9d0f4-9bc9-4e49-8538-5e00c7b6d7de" />



```python
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for obj in mat:
        if not isinstance(obj, (list, tuple)):
            raise TypeError(f"Элемент {obj} не является списком или кортежем")
        else:
            for item in obj:
                result.append(item)
    return result
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], 'ab']))
print(flatten([1, 2],(3, 4, 5)))
```

### Описание программы
Эта программа на Python преобразует список списков или кортежей в одномерный список.


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-06_20-42-16" src="https://github.com/user-attachments/assets/e8ff9b10-4dc7-47db-a54c-2fbba97fe4d0" />


## Задание B
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    rowlenght = len(mat[0])
    for row in mat:
        if len(row) != rowlenght:
            raise ValueError
    return [[row[index] for row in mat] for index in range(rowlenght)]
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([[]]))
print(transpose([[1, 2], [3]]))
```

### Описание программы
Данная программа реализует функцию transpose(), которая выполняет транспонирование матрицы - операцию, при которой строки матрицы становятся столбцами, а столбцы - строками.


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-06_22-40-21" src="https://github.com/user-attachments/assets/d982a33d-8330-4d24-89fe-99eb32793145" />


```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    rowlenght = len(mat[0])
    for row in mat:
        if len(row) != rowlenght:
            raise ValueError
    return [sum(row) for row in mat]
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
```


### Описание программы
Эта программа на Python вычисляет суммы элементов каждой строки в матрице (двумерном списке).


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-06_22-53-53" src="https://github.com/user-attachments/assets/3dc1365c-8efc-4420-b73a-27210bccb772" />


```python
def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    if len(mat) == 0:
        return []
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")
    newmat = transpose(mat)
    return [sum(row) for row in newmat]
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```


### Описание программы
Эта программа на Python вычисляет суммы столбцов матрицы.


### Пример выполнения
<img width="1920" height="1200" alt="2025-10-07_07-33-18" src="https://github.com/user-attachments/assets/ecca3f04-2069-4b28-98e0-5d9b3a9fd57b" />



## Задание С
```python
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
print(format_record(["Иванов Иван Иванович", "BIVT-25", 4.6]))
print(format_record(["Петров Пётр", "IKBO-12", 5.0]))
print(format_record(["  сидорова  анна   сергеевна ", "ABB-01", 3.999]))

```

### Описание программы
Эта программа на Python предназначена для форматирования записей о студентах в единый стандартизированный вид.


### Пример выполнения
<img width="1920" height="1200" alt="ex C Kolesnichenko Daria" src="https://github.com/user-attachments/assets/aa4d5847-1625-4563-ad47-279230bbaa70" />

















