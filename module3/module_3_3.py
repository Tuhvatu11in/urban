def print_params(a=1, b='строка', c=True):
  print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()  # Вывод: 1 строка True
print_params(10)  # Вывод: 10 строка True
print_params(10, 'новый текст')  # Вывод: 10 новый текст True
print_params(10, 'новый текст', False)  # Вывод: 10 новый текст False

# Вызовы с именованными аргументами
print_params(b=25)  # Вывод: 1 25 True
print_params(c=[1, 2, 3])  # Вывод: 1 строка [1, 2, 3]

# Распаковка параметров
values_list = [2, 'новая строка', False]
values_dict = {'a': 3, 'b': 'другая строка', 'c': True}

print_params(*values_list)  # Вывод: 2 новая строка False
print_params(**values_dict)  # Вывод: 3 другая строка True

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Вывод: 54.32 Строка 42
