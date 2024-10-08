class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

lion = Predator("Лев")
tiger = Predator("Тигр")
deer = Mammal("Олень")

rose = Flower("Роза")
apple = Fruit("Яблоко")
mushroom = Flower("Гриб")

# Проверка работы метода eat
lion.eat(apple)  # Лев съест яблоко
tiger.eat(rose)  # Тигр не станет есть розу
deer.eat(mushroom)  # Олень не станет есть гриб
