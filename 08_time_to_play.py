"""
1) udělejte jednoduchou hru:

# pomocí modulu random vygenerujte náhodné číslo od 1 do 10

pak pomocí while True:
od uživatele získejte číslo
a pokud je toto číslo stejné jako vygenerované číslo před while cyklem
tak ukončete while cyklus, a vypište mu to dané číslo



Jak to udělat:
1) do proměnné cislo si vygeneruji náhodné číslo
2) while True:
3) od uživatele získam hodnotu pomocí input
4) porovnám zadonou hodnu s vygenerovaným číslem (pozor na datové typy)
5) pokud je shoda, ukončím cyklus pomocí break

v opačním případě nic nedělám a cyklus by se měl dále ptát na další číslo
"""

import random 

while True:
    user_number = input("Ahoj uživateli, výběr je na tobě. Vyber číslo od 1 - 10: ")
    random_number = random.randint(0, 10)
   
    if random_number == int(user_number):
        print(f"Blahopřeji, trefa. Čísla {user_number} a {random_number} jsou ve shodě.")
        break
    else:
        print(f"Čísla {user_number} a {random_number} se neshodují, zkus to znovu.")
    