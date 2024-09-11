def custom_write(file_name, strings):

    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, 1):
            strings_positions[(i, file.tell())] = string
            file.write(string + '\n')
    return strings_positions

# Пример использования
strings = ['Text for tell.', 'Используйте кодировку utf-8.']
file_name = 'test.txt'

positions = custom_write(file_name, strings)
print(positions)
