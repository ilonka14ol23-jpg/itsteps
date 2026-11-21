result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b більше за 100")
    return a / b

# Замінили [] на порожній кортеж () або рядок "[]", щоб Python дозволив створити словник
data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        # Виправляємо опечатку: замість kem пишемо key
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        # Виводимо інформацію про виняток у консоль, щоб програма не зупинялася
        print(f"Стався виняток: {type(e).__name__}: {e}")

print("Фінальний результат:", result)