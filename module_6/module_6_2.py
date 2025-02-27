
class Vehicle:
    def __init__(self, owner, _model, __color, __engine_power):

        self.owner = owner                      # владелец транспорта (изменяемый)
        self._model = _model                    # модель(марка)транспорта (не изменяемый)
        self.__engine_power = __engine_power    # мощность двигателя (не изменяемый)
        self.__color = __color                  # название цвета (не изменяемый)

        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):            # возвращает строку: "Модель: <название модели транспорта>"
        return f'Модель: {self._model}'

    def get_horsepower(self):       # возвращает строку: "Мощность двигателя: <мощность>"
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):            # возвращает строку: "Цвет: <цвет транспорта>"
        return f'Цвет: {self.__color}'

    def print_info(self):           # распечатывает результаты методов:
        print(self.get_model())                         # модель
        print(self.get_horsepower())                    # мощность двигателя
        print(self.get_color())                         # цвет
        print(f'Владелец: {self.owner}')                # владелец

    def set_color(self, new_color):
        # принимает аргумент new_color(str), меняет цвет __color на new_color, если
        # он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
        # "Нельзя сменить цвет на <новый цвет>".

        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    pass


if __name__ == "__main__":

    # Пример результата выполнения программы:
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()

"""
Вывод на консоль:

Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: blue
Владелец: Fedos
Нельзя сменить цвет на Pink
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: BLACK
Владелец: Vasyok
"""


    
    

