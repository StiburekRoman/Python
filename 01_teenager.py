"""
vytvořte script, který zjistí jestli je věk teenager nebo ne:

teenager je od 13-19 let

uživatel zadá číslo (věk)

pokud je teenager, vypíše "jsi teenager"
jinak "nejsi teenager"

vytvořte nový repozitář nebo nahrajte existujícího repozitáře

jako test_teenager.py

"""

age = input("Ahoj náhodný uživateli, pochlub se svým věkem: ")
age = int(age)

if age >= 13 and age <= 19:
    print("Gratulujeme, prožíváš krásné a bezstarostné období. Jsi teenager.")
else:
    print("Nejsi teenegarem a nejspíš už máš to nejlepší za sebou. tak to tu nějak doklep")