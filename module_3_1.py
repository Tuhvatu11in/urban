calls = 0

def count_calls():
  global calls
  calls += 1

def string_info(string):
  count_calls()
  length = len(string)
  upper_string = string.upper()
  lower_string = string.lower()
  return length, upper_string, lower_string

def is_contains(string, list_to_search):
  count_calls()
  return string.lower() in [item.lower() for item in list_to_search]


print(string_info("Hello, world!")) 
print(is_contains("URBAN", ["city", "town", "URBAN"])) 
print(string_info("Python")) 
print(is_contains("apple", ["banana", "orange", "apple"])) 

print("Всего вызовов функций:", calls)
