def personal_sum(numbers):

  result = 0
  incorrect_data = 0
  for number in numbers:
    try:
      result += number
    except TypeError:
      incorrect_data += 1
  return result, incorrect_data

def calculate_average(numbers):
  try:
    sum, incorrect_data = personal_sum(numbers)
    if len(numbers) == 0:
      return 0
    else:
      return sum / len(numbers)
  except TypeError:
    print('В numbers записан некорректный тип данных')
    return None
