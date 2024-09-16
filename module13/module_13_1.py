import asyncio
import time

async def start_strongman(name, power):

    print(f'Силач {name} начал соревнования.')

    for i in range(1, 6):
        # Задержка обратно пропорциональна силе
        await asyncio.sleep(5 / power)
        print(f'Силач {name} поднял {i} шар')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():

    # Создаем 3 задачи для силачей
    task1 = asyncio.create_task(start_strongman("Иван", 3))
    task2 = asyncio.create_task(start_strongman("Петр", 2))
    task3 = asyncio.create_task(start_strongman("Алексей", 4))

    # Ставим каждую задачу в ожидание
    await task1
    await task2
    await task3

# Запускаем турнир
asyncio.run(start_tournament())
