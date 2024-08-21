
class Vehicle:
    owner = str()
    __model = str()
    __engine_power = int()
    __color = str()
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power
    def get_model(self,__model):
         print(f'Модель: {self.__model}')
    def  get_horsepower(self,__engine_power):
        print(f'Мощность двигателя: {self.__engine_power}')
    def get_color(self, __color):
        print(f'Цвет:{self.__color}')
    def  print_info(self):
        self.get_model(self.__model)
        self.get_horsepower(self.__engine_power)
        self.get_color(self.__color)
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        for i in range(len(new_color)):
            if new_color.lower() in self.__COLOR_VARIANTS:
                self.__color = new_color
            else:
               print(f'Нельзя сменить цвет на {new_color}')
               return i
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue',  500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'


vehicle1.print_info()










