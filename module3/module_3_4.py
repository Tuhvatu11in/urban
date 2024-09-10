def single_root_words(root_word, *other_words):

  same_words = []
  root_word = root_word.lower()  # Приводим root_word к нижнему регистру
  for word in other_words:
    word = word.lower()  # Приводим word к нижнему регистру
    if root_word in word or word in root_word:
      same_words.append(word)
  return same_words

# Вызов функции и вывод результата
result = single_root_words('дом', 'домик', 'дерево', 'домовладение', 'домашний')
print(result)  # Вывод: ['домик', 'домовладение', 'домашний']
