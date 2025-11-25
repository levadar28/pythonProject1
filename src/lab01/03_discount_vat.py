price = input("Введите цену: ").strip().replace(",", ".")
discount = input("Введите скидку: ").strip().replace(",", ".")
vat = input("Введите НДС: ").strip().replace(",", ".")

price = float(price)
discount = float(discount)
vat = float(vat)

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"База после скидки: {base:.2f}")
print(f"НДС: {vat_amount:.2f}")
print(f"Итого к оплате: {total:.2f}")
