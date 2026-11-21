def check_age(age):
    try:
        assert age >= 18, "Вам має бути 18 років або більше"
        print("Ви можете використовувати цей сервіс")
    except AssertionError as error:
        print(error)


# Перевірка роботи функції
check_age(20)
check_age(15)
