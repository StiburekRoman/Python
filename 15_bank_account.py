"""
vytvořte soubor 15_back_account.py

bude obsahovat třídu BankAccount (Bankovní účet)
atributy:
- owner (str) - jméno vlastníka účtu
- balance (int) - stav konta

oba atributy lze zadat v __init__, balance bude mít defaultně hodnotu 0 pokud není zadáno jinak

Metody:
- deposit (vklad)
- withdraw (výběr)
- print (vytiskne stav konta) - jméno a aktuální stav

Příklad použití:

muj_ucet = BankAccount('Jan Novák', 1000)
muj_ucet.deposit(10000)
muj_ucet.withdraw(500)
muj_ucet.print()
"""

class BankAccount:
    def __init__(self, owner, balance= 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance

    def withdraw(self, withdraw):
        self.balance -= withdraw
        return self.balance

    def info(self):
        if self.balance >= 0:
           print(f"Vlastníkem tohoto účtu je: {self.owner} a jeho aktuální stav je: {self.balance} ,- kč")
        else:
            print(f"Vlastníkem tohoto účtu je: {self.owner} a jeho aktuální stav je: {self.balance} ,- kč a proto jsme Vám zaktivovali kontokorent")

bezny_ucet = BankAccount("Donald Trump", 2450)

bezny_ucet.deposit(1000)
bezny_ucet.withdraw(4000)

bezny_ucet.info()