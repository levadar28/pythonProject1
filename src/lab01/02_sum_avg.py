a = "3,5"
b = "4,25"

print(f"a={a},b = {b}")

a = float(a.replace(',', '.'))
b = float(b.replace(',', '.'))

sum_result = a + b
avg_result = sum_result / 2

print(f"sum={sum_result:.2f}; avg={avg_result:.2f}")