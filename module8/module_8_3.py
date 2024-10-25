class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, name, vin, numbers):
        self.name = name

        # Проверка VIN перед присвоением
        if not self.__is_valid_vin(vin):
            raise IncorrectVinNumber('Некорректный vin номер')
        self.__vin = vin

        # Проверка номеров перед присвоением
        if not self.__is_valid_numbers(numbers):
            raise IncorrectCarNumbers('Некорректные номера')
        self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            return False
        if not 1000000 <= vin_number <= 9999999:
            return False
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            return False
        if len(numbers) != 6:
            return False
        return True

