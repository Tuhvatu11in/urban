first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Создание first_result
first_result = [len(string) for string in first_strings if len(string) >= 5]

# Создание second_result
second_result = []
for first_string in first_strings:
 for second_string in second_strings:
  if len(first_string) == len(second_string):
   second_result.append((first_string, second_string))

# Создание third_result
third_result = {}
for string in first_strings + second_strings:
 if len(string) % 2 == 0:
  third_result[string] = len(string)

# Вывод результатов
print(f"first_result: {first_result}")
print(f"second_result: {second_result}")
print(f"third_result: {third_result}")
