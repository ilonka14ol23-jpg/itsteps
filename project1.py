import colorama
from colorama import Fore, Back, Style, init

# Ініціалізація Colorama (метод init робить кольори кросплатформними,
# а параметр autoreset=True автоматично скидає колір після кожного рядка)
init(autoreset=True)

print("=" * 60)
print("1. ІНТРОСПЕКЦІЯ (ДОСЛІДЖЕННЯ) БІБЛІОТЕКИ COLORAMA:")
print("=" * 60)

# Функція dir() показує всі доступні атрибути та методи бібліотеки
print("Список основних елементів у модуль colorama:")
print(dir(colorama))

# Виводимо ключові атрибути для кольорів тексту (Fore) без службових змінних
fore_attributes = [attr for attr in dir(Fore) if not attr.startswith('_')]
print(f"\nАтрибути Fore (кольори шрифту): {fore_attributes}")

# Виводимо ключові атрибути для стилів тексту (Style)
style_attributes = [attr for attr in dir(Style) if not attr.startswith('_')]
print(f"Атрибути Style (стилі тексту): {style_attributes}")


print("\n" + "=" * 60)
print("2. КОМЕНТАРІ ТА ДЕМОНСТРАЦІЯ РОБОТИ ОСНОВНИХ КОМПОНЕНТІВ:")
print("=" * 60)

# Атрибути Fore (Fore.GREEN, Fore.RED тощо) — відповідають за колір самого тексту.
print(Fore.GREEN + "Цей текст виведено зеленим кольором за допомогою Fore.GREEN")

# Атрибути Back (Back.YELLOW, Back.BLUE тощо) — відповідають за колір фону (заднього плану).
print(Fore.BLACK + Back.YELLOW + "Цей текст чорного кольору на жовтому фоні (Back.YELLOW)")

# Атрибути Style (Style.BRIGHT, Style.DIM тощо) — керують інтенсивністю та жирністю тексту.
print(Style.BRIGHT + Fore.RED + "Цей текст яскравий і червоний (Style.BRIGHT + Fore.RED)")

# Метод/функція deinit() - скасовує дію colorama і повертає термінал до стандартного вигляду.
colorama.deinit()
print("Після виклику deinit() кольори повертаються до стандартних системних.")