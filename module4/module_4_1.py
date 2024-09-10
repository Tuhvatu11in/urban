# файл fake_math.py
def divide(first, second):

  if second == 0:
    return 'Ошибка'
  else:
    return first / second

# файл true_math.py
from math import inf

def divide(first, second):

  if second == 0:
    return inf
  else:
    return first / second

# файл module_4_1.py
from fake_math import divide as fake_divide
from true_math import divide as true_divide

first_number = 10
second_number = 0

fake_result = fake_divide(first_number, second_number)
true_result = true_divide(first_number, second_number)

print(f"Результат деления (fake_math): {fake_result}")
print(f"Результат деления (true_math): {true_result}")
