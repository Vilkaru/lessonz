class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
    def __eq__(self, other = int):
        return self.number_of_floors == other
    def __lt__(self, other = int):
        return self.number_of_floors < other
    def __le__(self, other = int):
        return self.number_of_floors <= other
    def __gt__(self, other = int):
        return self.number_of_floors > other
    def __ne__(self, other = int):
        return self.number_of_floors != other
    def __ge__(self, other = int):
        return self.number_of_floors >= other
    def __add__(self, value):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors + value}')
    def __radd__(self, value):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors + value}')
    def  __iadd__(self, other):
        self.number_of_floors += other
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1.number_of_floors == h2.number_of_floors) # __eq__

h1.number_of_floors = h1.number_of_floors + 10 # __add__
print(h1)
print(h1.number_of_floors == h2.number_of_floors)

h1.number_of_floors += 10 # __iadd__
print(h1)

h2.number_of_floors = 10 + h2.number_of_floors # __radd__
print(h2)

print(h1.number_of_floors > h2.number_of_floors) # __gt__
print(h1.number_of_floors >= h2.number_of_floors) # __ge__
print(h1.number_of_floors < h2.number_of_floors) # __lt__
print(h1.number_of_floors <= h2.number_of_floors) # __le__
print(h1.number_of_floors != h2.number_of_floors) # __ne__




            



    















