# suite_12_3.py
import unittest

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
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
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


suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

result = runner.run(suite)
