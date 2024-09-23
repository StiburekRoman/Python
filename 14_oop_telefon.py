"""
vytvořte 14_oop_telefon.py

vytvořte třídu MobilePhone

vymyslete k této třídě smysluplné atributy a metody
- 3-5 atributy (jaké vlastnosti a parametry by mohl mít mobilní telefon?)
- 2 metody (jaké chování (metody) by telefon mohl mít?)

vytvořte 2 instance
"""

class MobilePhone:
        def __init__(self, memory, procesor, size, displey):
                self.memory = memory
                self.procesor = procesor
                self.size = size
                self.displey = displey
                self.contacts = set()
                self.songs = set()

        def save_contact (self, contact: "MobilePhone"):
                if self is not contact:
                        self.contacts.add(contact)
                else:
                        print("Toto jménu již v seznamu existuje, zkuste jiné")

        def save_song (self, song):
                if self is not song:
                        self.songs.add(song)


        def send_message(self, contact):
                message = input("Zadejte zpráve kterou chcete poslat svéhu příteli: ")
                if contact in self.contacts:
                        print(f"Zpráva: {message}. byla odeslána")
                else: 
                        print("Zadené jméno není mezi kontakty")

              
        
        

samsungA40 = MobilePhone(128, "Qualcomm Snapdragon 870", 6.8, "AMOLED")
lg = MobilePhone(64, "MediaTek Helio G80", 6.1, "IPS LCD")


samsungA40.save_song("ŠKWOR - Síla starých vín")

lg.save_contact("Milenka")
lg.send_message("Milenka")


print(lg.contacts)
print(samsungA40.songs)


        

            