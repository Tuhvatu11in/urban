def single_root_words(root_word, *other_words):
  same_words = []
  for word in other_words:
    if root_word in word or word in root_word:
      same_words.append(word)
  return same_words

result = single_root_words('дом', 'домик', 'дерево', 'домовладение', 'домашний')
print(result)  # Вывод: ['домик', 'домовладение', 'домашний']
