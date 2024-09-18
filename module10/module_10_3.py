import threading
import random
import time

class Lock:
    def __init__(self):
        self._locked = False

    def acquire(self):
        self._locked = True

    def release(self):
        self._locked = False

    def locked(self):
        return self._locked

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)  # имитация задержки

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

    def run(self):
        deposit_thread = threading.Thread(target=self.deposit)
        take_thread = threading.Thread(target=self.take)

        deposit_thread.start()
        take_thread.start()

        deposit_thread.join()
        take_thread.join()

        print(f"Итоговый баланс: {self.balance}")

if __name__ == "__main__":
    bank = Bank()
    bank.run()
