"""
vytvořte soubor 11_graf.py

vytvořte sloupcový graf (bar chart) pomocí matplotlib:

data = {
    'Praha': 1_384_732,
    'Brno': 400_566,
    'Ostrava': 284_765,
    'Plzeň': 185_599,
}

ukázku máte v test_bar_chart.py
je možné že data budete muset upravit nebo použit nějaké dict metody,
aby jste dostali vhodné vstupy pro graf
"""

import matplotlib.pyplot as plt

data = {
    'Praha': 1_384_732,
    'Brno': 400_566,
    'Ostrava': 284_765,
    'Plzeň': 185_599,
    'České Budějovice': 93_984,
    'Divišov': 1_810,
}

city, population = zip(*data.items())

colors = ["Blue", "Green", "Aqua", "Purple", "Yellow"]



plt.figure(figsize=(12, 8))
plt.bar(city, population, color= colors, width=0.3)
plt.title("Population Czech cities", fontsize= 18)
plt.xlabel("cities", fontsize= 18)
plt.ylabel("population", fontsize= 18)
plt.show()  


