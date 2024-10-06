
"""

Stat
Mesto

oba budou mít název, mesto bude mít referenci na stát
Mesto tedy na venek dokáže zjistit název státu ke kterému patří
Mesto bude mít metodu info, která vypíše:
- "Město ABC leží ve státě XYZ"

Bonusový úkol:
Stat bude mít metodu info, která dokáže zjistit, kolik má měst
- implementaci nechám na vás

použití:

dansko = Stat('Dansko')
norsko = Stat('Norsko')

kodan = Mesto('Kodaň', dansko)
hovedstaden = Mesto('Hovedstaden', dansko)

oslo = Mesto('Oslo', norsko)

oslo.info() # vypíše "Město Oslo leží ve státě Norsko"
kodan.info() # vypíše "Město Kodan leží ve státě Dánsko"

"""


class Stat:
    def __init__(self, nazev):
        self.nazev = nazev
        self.mesta = []  # seznam pro města, která patří do tohoto státu

    def pridej_mesto(self, mesto):
        self.mesta.append(mesto)

    def info(self):
        print(f"Stát {self.nazev} má {len(self.mesta)} měst(a).")


class Mesto:
    def __init__(self, nazev, stat):
        self.nazev = nazev
        self.stat = stat
        stat.pridej_mesto(self)
        

    def info(self):
        print(f"Město {self.nazev} leží ve státě {self.stat.nazev}")



dansko = Stat('Dansko')
norsko = Stat('Norsko')

kodan = Mesto('Kodaň', dansko)
hovedstaden = Mesto('Hovedstaden', dansko)

oslo = Mesto('Oslo', norsko)


oslo.info()      
kodan.info()     


dansko.info()      
norsko.info()      