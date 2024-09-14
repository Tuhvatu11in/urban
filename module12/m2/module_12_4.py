# tests_12_4.py
import unittest
import logging

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).name}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("Bob")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_init(self):
        self.assertEqual(self.runner.name, "Bob")
        self.assertEqual(self.runner.distance, 0)
        self.assertEqual(self.runner.speed, 5)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            self.runner = Runner(123)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            self.assertRaises(TypeError)
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            self.runner = Runner("Bob", -5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            self.assertRaises(ValueError)
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_str(self):
        self.assertEqual(str(self.runner), "Bob")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_eq_with_string(self):
        self.assertTrue(self.runner == "Bob")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_eq_with_runner(self):
        other_runner = Runner("Bob")
        self.assertTrue(self.runner == other_runner)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_eq_with_different_runner(self):
        other_runner = Runner("Alice")
        self.assertFalse(self.runner == other_runner)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.runner1 = Runner("Bob")
        self.runner2 = Runner("Alice", speed=7)
        self.tournament = Tournament(20, self.runner1, self.runner2)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_init(self):
        self.assertEqual(self.tournament.full_distance, 20)
        self.assertEqual(self.tournament.participants, [self.runner1, self.runner2])

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_start(self):
        finishers = self.tournament.start()
        self.assertEqual(len(finishers), 2)
        self.assertEqual(finishers[1].name, "Alice")
        self.assertEqual(finishers[2].name, "Bob")


# Создаем TestSuite
suite = unittest.TestSuite()

# Добавляем тесты в TestSuite
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Создаем TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем тесты
result = runner.run(suite)
