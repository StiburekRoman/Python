mesta_cr = {
    "Praha": 1300000,
    "Brno": 380000,
    "Ostrava": 290000,
    "Plzeň": 170000,
    "Liberec": 100000,
    "Olomouc": 100000,
    "Ústí nad Labem": 92000,
    "Hradec Králové": 93000,
    "České Budějovice": 94000,
    "Pardubice": 90000
}

def info(name_city):
    try:
        print(name_city, mesta_cr[name_city])
    except KeyError:
        print("Neznámé město")
         

info("New York")
