class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products_string = file.read()
        return products_string

    def add(self, *products):
        existing_products = set()
        with open(self.__file_name, 'r') as file:
            for line in file:
                existing_products.add(line.split(',')[0].strip())

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in existing_products:
                    file.write(f"{product}\n")
                else:
                    print(f'Продукт {product.name} уже есть в магазине')


# Пример использования
potato = Product('Potato', 50.0, 'Vagetables')
apple = Product('Apple', 10.5, 'Fruits')
milk = Product('Milk', 1.0, 'Dairy')

shop = Shop()
print(shop.get_products())  # Выведет содержимое файла products.txt

shop.add(potato, apple, milk)
shop.add(potato)  # Выведет сообщение, что Potato уже есть в магазине

print(shop.get_products())
