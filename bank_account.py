вот такой:
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def info(self):
        print(f'Владелец счёта: {self.owner}')
        print(f'Баланс счёта: ${self.balance}')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено {amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма внесения должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Недостаточно средств! Доступно только {self.balance}')
        elif amount <= 0:
            print("Сумма снятия должна быть положительной.")
        else:
            self.balance -= amount
            print(f'Снято {amount}. Остаток: {self.balance}')


# Создаём экземпляр класса
acct1 = Account('Влад', 100)

# Выводим информацию
acct1.info()

# Вносим и снимаем деньги
acct1.deposit(50)     # Внесено 50. Новый баланс: 150
acct1.withdraw(30)    # Снято 30. Остаток: 120
acct1.withdraw(200)   # Недостаточно средств! Доступно только 120
acct1.deposit(-10)    # Сумма внесения должна быть положительной.
acct1.withdraw(-5)    # Сумма снятия должна быть положительной.

# Проверяем итог
acct1.info()