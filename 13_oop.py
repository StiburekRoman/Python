"""
1. podívejte se na algoritmus přátelství 
https://www.youtube.com/watch?v=nUHbVRSLlEs

2. můžete se podívat na buble sort zde:
https://www.geeksforgeeks.org/bubble-sort-algorithm/


3. vytvořte soubor 13_oop.py
a v něm třídu Planeta, která bude obsahovat:
atributy:
- poradi 
- nazev

a metodu info
která řekne "Toto je [název planety] a je [pořadí] od Slunce"

vytvořte 2 instance
- Země
- a nějakou další planetu"""


class planet:
    def __init__(self, nazev, poradi):
        self.name = nazev
        self.poradi = poradi
    
    def info(self):
        print(f"Toto je {self.name} a je {self.poradi} od Slunce")

Jupiter = planet("Jupiter", "pátý")
Merkur = planet("Merkur", "první")

Jupiter.info()
Merkur.info()