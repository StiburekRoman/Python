"""
1) vytvořte soubor 03_funkce.py

v souboru vytvořte funkci:

def test_heslo(heslo: str):

tato funkce otestuje, zda uživatel zadal heslo alespoň o délce 5 znaků

test_heslo('1234') # vrátí False
test_heslo('12345') # vrátí True
test_heslo('TajnéHeslo') # vrátí True

"""


def test_heslo(heslo):
    if len(heslo) >= 5:
        return True
    else: 
        return False


print(test_heslo("175495"))

print(test_heslo("jkasdjlfjasdklf"))

print(test_heslo("1756"))
