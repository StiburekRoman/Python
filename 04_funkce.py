"""
Vytvořte soubor 04_funkce.py

ve kterém budou 2 funkce:

1) funkce pro výpočet obsahu kruhu
2) funkce pro vpočet obvodu kruhu

vstupní parametr bude poloměr


Viz zde:
https://www.umimeto.org/asset/system/um/img/rules/ilustrace-obsah-obvod-prehled.png


řecké písmeno PI definujte jako 3.14 nebo importujte modul math, kde se nachází konstanta pi

import math

print(math.pi)

obě funkce otestujte

"""
import math

r = input("Zadejte poloměr kruhu: ")
r = int(r)
value_Pi = math.pi


def obsah_kruhu(r: int, value_Pi: int):  
    S = value_Pi * r ** 2
    return S


def obvod_kruhu(r: int, value_Pi: int):
   O = 2 * value_Pi * r
   return O

print(obsah_kruhu(r, value_Pi))
print(obvod_kruhu(r, value_Pi))