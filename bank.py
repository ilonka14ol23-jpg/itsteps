class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float = 0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        """Поповнення рахунку"""
        if amount > 0:
            self.balance += amount
            print(f"Рахунок {self.account_number} поповнено на {amount} грн. Баланс: {self.balance} грн.")
        else:
            print("Сума поповнення має бути більшою за нуль.")

    def withdraw(self, amount: float):
        """Зняття коштів"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"З рахунку {self.account_number} знято {amount} грн. Залишок: {self.balance} грн.")
            return True
        else:
            print(f"Недостатньо коштів на рахунку {self.account_number} або некоректна сума.")
            return False

    def __str__(self):
        return f"Рахунок №{self.account_number} (Власник: {self.owner}), Баланс: {self.balance} грн."


class Bank:
    def __init__(self):
        self.accounts = {}  # Словник для зберігання рахунків (номер -> об'єкт BankAccount)

    def add_account(self, account: BankAccount):
        """Додавання нового рахунку до банку"""
        self.accounts[account.account_number] = account
        print(f"Створено рахунок №{account.account_number} для власника {account.owner}.")

    def transfer(self, from_account_number: str, to_account_number: str, amount: float):
        """Переказ коштів між рахунками"""
        if from_account_number not in self.accounts or to_account_number not in self.accounts:
            print("Помилка переказу: один із рахунків не знайдено.")
            return

        from_acc = self.accounts[from_account_number]
        to_acc = self.accounts[to_account_number]

        print(f"Спроба переказу {amount} грн з рахунку {from_account_number} на {to_account_number}...")

        # Спершу намагаємося зняти кошти з рахунку відправника
        if from_acc.withdraw(amount):
            to_acc.deposit(amount)
            print("Переказ успішно виконано!")
        else:
            print("Переказ скасовано через відсутність коштів.")


# --- Приклад використання ---
if __name__ == "__main__":
    my_bank = Bank()

    # Створюємо рахунки
    acc1 = BankAccount("Ілона Яценко", "UA111", 1000.0)
    acc2 = BankAccount("Олександр", "UA222", 500.0)

    my_bank.add_account(acc1)
    my_bank.add_account(acc2)

    print("-" * 30)
    # Поповнення
    acc1.deposit(250)

    print("-" * 30)
    # Переказ між рахунками
    my_bank.transfer("UA111", "UA222", 300)

    print("-" * 30)
    # Перевірка фінального балансу
    print(acc1)
    print(acc2)