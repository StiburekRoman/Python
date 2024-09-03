"""
1. práce s dict
vytvořte soubor 10_dict.py
kde bude:
ceny_potravin = {
    'máslo': 30,
    'chleba': 20,
    'sýr': 30,
    'jablko': 5
}

a) přidejte novou položku 'mléko' s částkou 25
b) zjistete, který produkt je nejlevnější
c) kolik mě bude stát, když si koupím 4x jablka, 1x máslo, a 2x sýr
udělejte printy pro kontrolu
"""


ceny_potravin = {
    'máslo': 30,
    'chleba': 20,
    'sýr': 30,
    'jablko': 5
}

ceny_potravin["mléko"] = 25

print(ceny_potravin)


max_sum = 0

for value in ceny_potravin.values():
    if max_sum < value:
        max_sum = value

min_suma = max_sum          # Nastavení reálného největšího čísla pro možné porovnávání
item_for_min = ""

for key, value in ceny_potravin.items():
    if min_suma > value:
        min_suma = value
        item_for_min = key

print(f"Nejlevnější je", item_for_min, "a stojí", min_suma, "kč")
print(f"Nejlevnější produkt je:", item_for_min)


for key, value in ceny_potravin.items():
    if key == "jablko":
        apple = 4 * value
    if key == "máslo":
        butter = value
    if key == "sýr":
        cheese = 2* value
    
suma = apple + butter + cheese

print(suma)



