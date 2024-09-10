class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

# Создаем объект класса House
my_house = House("ЖК Эльбрус", 30)

# Вызываем метод go_to
my_house.go_to(5)  # Пример вызова для перехода на 5 этаж
