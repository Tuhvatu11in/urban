my_string = input("Введите произвольный текст: ")

print(f"Количество символов в тексте: {len(my_string)}")

print(f"В верхнем регистре: {my_string.upper()}")
print(f"В нижнем регистре: {my_string.lower()}")

my_string = my_string.replace(" ", "")
print(f"Без пробелов: {my_string}")

print(f"Первый символ: {my_string[0]}")

print(f"Последний символ: {my_string[-1]}")
