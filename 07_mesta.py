"""
soubor se bude jmenovat 07_mesta.py

máme tato data se sloupci
1. nazev
2. pocet_obyvatel
3. rozloha

eu_cities = [
    ['Berlín', 3669491, 891],
    ['Madrid', 3223334, 604],
    ['Řím', 2872800, 1285],
    ['Paříž', 2165423, 105],
    ['Bukurešť', 1883425, 228],
    ['Budapešť', 1746344, 525],
    ['Varšava', 1790658, 517],
    ['Vídeň', 1921153, 414],
    ['Hamburk', 1841179, 755],
    ['Barcelona', 1620343, 101]
]

pomocí for cyklu zjistěte:
1) jaký je celkový počet obyvatel v těchto městech
2) které město má nejvíce a nejměně obyvatel

"""

eu_cities = [
    ['Berlín', 3669491, 891],
    ['Madrid', 3223334, 604],
    ['Řím', 2872800, 1285],
    ['Paříž', 2165423, 105],
    ['Bukurešť', 1883425, 228],
    ['Budapešť', 1746344, 525],
    ['Varšava', 1790658, 517],
    ['Vídeň', 1921153, 414],
    ['Hamburk', 1841179, 755],
    ['Barcelona', 1620343, 101]
]



total_number_resident = 0

for resident in eu_cities:
    total_number_resident += resident[1]
   
print(f"Celkový počet obyvatel z našeho seznamu měst je: {total_number_resident}")


max_resident = 0
min_resident = eu_cities[1][1]

for resident in eu_cities:
    number_of_resident = resident[1]
    if number_of_resident > max_resident:
        max_resident = number_of_resident
    
    if number_of_resident < min_resident:
        min_resident = number_of_resident

print(f"Z našeho seznamu měst je nejvíce obyvatel: {max_resident} a nejméně obyvatel: {min_resident}")


