def test_function():
  """
  Функция test_function, содержащая внутреннюю функцию.
  """
  def inner_function():
    """
    Внутренняя функция, доступная только в области видимости test_function.
    """
    print("Я в области видимости функции test_function")

  inner_function()  # Вызов inner_function внутри test_function

# Вызов test_function
test_function()

# inner_function()  # Ошибка: "NameError: name 'inner_function' is not defined"
