"""задачка 2 с метанита
Создайте класс BankAccount, который представляет банковский счет. Определите в этом классе атрибуты account_number и balance, которые представляют номер счета и баланс.
Через параметры конструктора передайте этим атрибутам начальные значения.
Также в классе определите метод add, который принимает некоторую сумму и добавляет ее на баланс счета. И определите метод withdraw, который принимает некоторую сумму и снимает ее с баланса.
При этом с баланса нельзя снять больше, чем имеется. Если на балансе недостаточно средств, то пользователю должно выводиться соответствующее сообщение."""

class BankAccount:

    def __init__(self):
        acc_num = 123456789
        bal = 5400
        self.account_number = acc_num
        self.balance = bal
        print(f"Ваш счёт {self.account_number}. У вас на счету {self.balance}")

    #def __del__(self):
    #    print("Ваш счёт успешно закрыт")

    def add(self, x):
        self.balance += x
        print(f"На ваш счёт зачислено {x}. Всего на счету {self.balance}" )

    def withdraw(self, x):
        if x > self.balance:
            print(f"Неудачная попытка списания {x}. Недостаточно средств для списания. Ваш баланс {self.balance}")
        else:
            self.balance -= x
            print(f"Со счёта списано {x}. Остаток по счёту {self.balance}")


cart1 = BankAccount()
cart1.add(600)
cart1.add(10000)
cart1.withdraw(15000)
cart1.withdraw(1500)
cart1.add(32000)






