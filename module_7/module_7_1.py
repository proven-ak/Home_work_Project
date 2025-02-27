# Задача "Учёт товаров":

class Product:
    # Атрибут name - название продукта (строка).
    # Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
    # Атрибут category - категория товара (строка).
    # Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
    # Все данные в строке разделены запятой с пробелами.

    def __init__(self, name, weight, category):
        self.name = name                            # название продукта(строка)
        self.weight = weight                        # общий вес товара(дробное число) (5.4, 52.8 и т.п.).
        self.category = category                    # категория товара(строка).

    def __str__(self):
        # Метод __str__, который возвращает строку в формате
        # '<название>, <вес>, <категория>'.
        # Все данные в строке разделены запятой с пробелами.

        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    # Инкапсулированный атрибут __file_name = 'products.txt'.
    # Метод get_products(self), который считывает всю информацию из файла __file_name,
    # закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
    # Метод add(self, *products), который принимает неограниченное количество объектов
    # класса Product. Добавляет в файл __file_name каждый продукт из products,
    # если его ещё нет в файле (по названию).
    # Если такой продукт уже есть, то не добавляет и выводит строку
    # 'Продукт <название> уже есть в магазине'.
    def __init__(self):
        self.__file_name = "products.txt"       # Инкапсулированное имя файла

    def get_products(self):
        # метод считывает всю информацию из файла __file_name, закрывает его
        # и возвращает единую строку со всеми товарами из файла __file_name.
        try:
            with open(self.__file_name, "r", encoding="utf-8") as file:
                # Считываем всё содержимое файла и удаляем лишние пробелы
                return file.read().strip()

        except FileNotFoundError:
            # Если файл не существует, возвращаем пустую строку
            return ""

    def add(self, *products):
        # Метод, который принимает неограниченное количество объектов
        # класса Product. Добавляет в файл __file_name каждый продукт из products,
        # если его ещё нет в файле (по названию).
        # Если такой продукт уже есть, то не добавляет и выводит строку
        # 'Продукт <название> уже есть в магазине'.

        # Получаем список текущих продуктов из файла
        current_data = self.get_products()                                          # текущие данные
        existing_products = current_data.split("\n") if current_data else []        # существующие продукты
        existing_names = [line.split(", ")[0] for line in existing_products]        # существующие имена

        with open(self.__file_name, "a", encoding="utf-8") as file:
            for product in products:
                if product.name in existing_names:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(str(product) + "\n")
                    print(f"Продукт {product.name} добавлен в магазин")


# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())

"""
Вывод на консоль:
Первый запуск:
Spaghetti, 3.4, Groceries
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables

Второй запуск:
Spaghetti, 3.4, Groceries
Продукт Potato уже есть в магазине
Продукт Spaghetti уже есть в магазине
Продукт Potato уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables
"""
