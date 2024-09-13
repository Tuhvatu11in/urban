import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, "r") as file:
        line = file.readline()
        while line:
            all_data.append(line.strip())
            line = file.readline()
    return all_data

if __name__ == "__main__":
    file_names = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]  # Замените на имена файлов в вашем архиве

    # Линейный вызов
    start_time = time.time()
    for file_name in file_names:
        read_info(file_name)
    end_time = time.time()
    print(f"Время выполнения линейного считывания: {end_time - start_time} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool(processes=5) as pool:  # Количество процессов можно изменять
        pool.map(read_info, file_names)
    end_time = time.time()
    print(f"Время выполнения многопроцессного считывания: {end_time - start_time} секунд")
