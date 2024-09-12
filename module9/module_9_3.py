first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для первого задания
first_result = (len(word1) - len(word2) for word1, word2 in zip(first, second) if len(word1) != len(word2))

# Генераторная сборка для второго задания
second_result = (len(first[i]) - len(second[i]) for i in range(len(first)))

print(f"first_result: {list(first_result)}")
print(f"second_result: {list(second_result)}")
