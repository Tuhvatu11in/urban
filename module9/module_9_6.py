def all_variants(text):
  for i in range(len(text) + 1):
    for j in range(i):
      yield text[j:i]

# Пример использования:
for variant in all_variants("abc"):
  print(variant)

