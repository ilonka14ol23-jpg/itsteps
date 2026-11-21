def calculator_decorator(func):
    def wrapper(expression):
        # Залишаємо тільки дозволені символи для безпеки
        allowed = "0123456789+-*/(). "
        for char in expression:
            if char not in allowed:
                return f"Помилка: неприпустимий символ '{char}'"

        try:
            result = func(expression)
            return f"{expression} = {result}"
        except ZeroDivisionError:
            return "Помилка: на нуль ділити не можна!"
        except SyntaxError:
            return "Помилка: неправильно записаний приклад."
        except Exception:
            return "Помилка обчислення."

    return wrapper


@calculator_decorator
def calculate(expression):
    return eval(expression)


# Перевірка
print(calculate("2 + 2 * 2"))
print(calculate("10 / 0"))
print(calculate("5 + * 3"))
print(calculate("2 + a"))
