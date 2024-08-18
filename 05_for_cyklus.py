"""vytvořte soubor 05_for_cyklus.py

v listu lze zapsat data i takto pod sebe:

kde budou data = [
    8848, # Mount Everest
    8611, # K2
    4808, # Mont Blanc
    5895, # Kilimanjaro
    3776, # Mount Fuji
    5642, # Elbrus
    1603, # Sněžka
    1492, # Praděd
    1323, # Lysá hora
]

logika bude následující:
for cyklem projděte všechny nadmořské výšky a pokud:
je hora nižší jak 3000 m - napište X je nizká výška
je hora 3000 m a více, ale zároveň méně jak 6000 m - napište X je střední výška
jinak napište X je vysoká výška
.. kde X je výška
"""

data = [
    ("Mount Everest", 8848),
    ("K2", 8611),
    ("Mont Blanc", 4808),
    ("Kilimandjaro", 5895),
    ("Mount Fuji", 3776),
    ("Elbrus", 5642),
    ("Snežka", 1603),
    ("Praděd", 1492),
    ("Lysá hora", 1323),
    ("Aconcagu", 6962),
    ("Nanga Parbat", 8162),
    ("Denali ", 6190),
    ("Kangchenjunga ", 8586),
]

small_high_mountain = []
medium_high_mountain = []
big_high_mountain = []
exciting_high_mountain = []

def compare_FAMSL(data):
    for name_mountain, high_mountain in data:
        
        if high_mountain < 3000:
            small_high_mountain.append(name_mountain)
           # print(f"{name_mountain} je vysoká: {high_mountain} a patří do kategorie menších hor")

        elif high_mountain >= 3000 and high_mountain < 6000:
            medium_high_mountain.append(name_mountain)
           # print(f"{name_mountain}  a patří do kategorie středních hor")

        elif high_mountain >= 6000 and high_mountain < 8000:
            big_high_mountain.append(name_mountain)
           # print(f"{name_mountain}  a patří do kategorie vysové hory a výstup může být velice náročný a nebezpečný")

        else:
            exciting_high_mountain.append(name_mountain)
           # print(f"{name_mountain}  a patří do té nejzajímavější kategorie. Takzvané osmitisícovky, jen pro ty zkušené a odvážné")

def write_out_mountain(small, medium, big, biggest):
    print(small)
    print(medium)
    print(big)
    print(biggest)

compare_FAMSL(data)
write_out_mountain(small_high_mountain, medium_high_mountain, big_high_mountain, exciting_high_mountain)

