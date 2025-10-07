fio_input = input("ФИО: ")

fio_cleaned = fio_input.strip()

words = fio_cleaned.split()
initials = ''.join(word[0].upper() for word in words if word)

print(f"Инициалы: {initials}.")
print(f"Длина символов: {len(fio_cleaned)}")