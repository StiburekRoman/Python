"""
1) Vytvořte si nový github repozitář,
který bude sloužit pro odevzdávání domácích úkolů
a pošlete mi na něj odkaz do teamsu

2) vytvořte 02_user.py kde
uživatel zadá své jmeno a věk pomocí input
uložte tyto informace do souboru
02_user.txt

poznámka:
prefix 02_ je tam kvuli tomu, že se o bude řadit podle názvu a bude jednoduše dohledatelné
pokud můžete přejmenujte první úkol na 01_test_teenager.py
děkuji :)
"""

user_input = input("Ahoj uživateli, zadej své jméno a věk ať se o tobě trošku dozvíme: ")


with open('task2.txt', 'w') as file:
    file.write(user_input)
