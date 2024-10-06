class Person:
    def __init__(self, name, mother=None, father=None):
        self.name = name
        self.mother = mother
        self.father = father

    def get_parents(self):
        return (self.mother, self.father)


john = Person('John')
lena = Person('Lena')

peter = Person('Peter', mother=lena, father=john)


print(peter.get_parents())  


print(lena.get_parents())  