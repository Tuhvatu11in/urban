import unittest

#  TestCase RunnerTest
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        print("Setup for RunnerTest")

    @classmethod
    def tearDownClass(cls):
        print("Teardown for RunnerTest")

    def test_run(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        print("Проверка метода run")

    def test_stop(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        print("Проверка метода stop")

#  TestCase TournamentTest
class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        print("Setup for TournamentTest")

    @classmethod
    def tearDownClass(cls):
        print("Teardown for TournamentTest")

    def test_start(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        print("Проверка метода start")

    def test_finish(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        print("Проверка метода finish")

#  TestSuite
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(test_suite)
