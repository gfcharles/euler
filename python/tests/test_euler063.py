from tests.test_euler import TestEuler, TestEulerSetup
from euler063 import euler063

class TestEuler063(TestEulerSetup, TestEuler):
    problem_number = 63
    function = euler063
