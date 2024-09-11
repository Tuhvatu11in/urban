import os
import time

def show_file_info(directory):

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            modified_time = time.ctime(os.path.getmtime(file_path))  # Использовать os.path.getctime()
            size = os.path.getsize(file_path)
            parent_dir = os.path.dirname(file_path)

            print(f"Файл: {file_path}")
            print(f"Время последнего изменения: {modified_time}")
            print(f"Размер: {size} байт")
            print(f"Родительская директория: {parent_dir}")
            print("-" * 20)

if __name__ == "__main__":
    directory = input("Введите путь к каталогу: ")
    show_file_info(directory)
