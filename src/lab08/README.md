Основные моменты реализации `models.py`
1. @dataclass: автоматически генерирует __init__, __repr__, __eq__ методы.

2. __post_init__: Выполняется после инициализации, используется для валидации:

* проверка формата даты с помощью datetime.strptime();

* проверка диапазона GPA.

3. age(): вычисляет полные годы на текущую дату с учётом месяца и дня рождения.

4. to_dict(): преобразует объект в словарь для последующей сериализации в JSON.

5. from_dict(): классовый метод для создания объекта из словаря (альтернативный конструктор).

6. __str__(): возвращает форматированную строку с читаемым представлением объекта.

7. Валидация:

* дата должна быть в формате YYYY-MM-DD;

* GPA должен быть в диапазоне 0-5.

### Пример вывода программы
<img width="1535" height="802" alt="models_laba08 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/042f837d-a50f-45ea-ab6a-a63a317fb55f" />

Основные особенности реализации `serialize.py`
* students_to_json(students, path):
1. Валидация входных данных: проверяет, что передан список и все элементы - объекты Student.

2. Сериализация: использует метод to_dict() каждого студента.

3. Обработка ошибок: перехватывает ошибки записи в файл.

4. Кодировка UTF-8: сохраняет кириллические символы корректно.

5. Человекочитаемый формат: использует indent=2 для красивого форматирования.

* students_from_json(path) -> list[Student]:
1. Чтение и парсинг JSON: с обработкой ошибок файловой системы и синтаксиса JSON.

2. Валидация структуры: проверяет, что JSON содержит массив.

3. Поэлементная обработка: создает объекты Student из каждого словаря.

4. Сбор ошибок: накапливает все ошибки валидации, а не останавливается на первой.

5. Комплексная обработка ошибок: включает проверку типов, обязательных полей и бизнес-логики.

### Примеры запуска
<img width="1643" height="719" alt="serialize_laba08 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/a88f9279-9231-4b02-8d3b-81650ae29364" />

### Пример содержимого файла students.json
<img width="662" height="820" alt="students_json_ laba08 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/e58b59c4-d5c6-458e-862a-32c3cb9e7f88" />

### Пример содержимого файла not_list.json
<img width="1213" height="942" alt="not_list_ json laba08 Kolsenichenko Daria" src="https://github.com/user-attachments/assets/703e8483-b710-45b5-b910-054c8724b834" />

### Пример содержимого файла invalid_data.json
<img width="1549" height="875" alt="invalid_data json laba08 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/1fceaee4-bcc7-43d1-b678-c2d48182ead5" />

### Пример содержимого файла incomplete.json
<img width="1855" height="558" alt="incomplete json laba08 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/bea0c879-b669-4e0e-a7a2-7b24b2a3fd51" />

### Пример содержимого файла invalid.json
<img width="1813" height="669" alt="invalid json laba08 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/ced75e74-510a-4cb3-b811-bcbdeae828f0" />

### Пример реализации входного JSON и выходного JSON
<img width="1649" height="831" alt="creating example files laba08 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/ec947032-54b2-4c01-9487-5c0f2d594396" />

## Пример входного JSON
<img width="1391" height="1011" alt="students_input json laba08 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/f98f5f5b-f297-49fb-8eac-ecaea1ecfceb" />

## Пример выходного JSON
<img width="1176" height="937" alt="students_output json laba08 Kolesnichenko Daria" src="https://github.com/user-attachments/assets/d25699b4-e7af-41d8-b485-ace049c86fe5" />