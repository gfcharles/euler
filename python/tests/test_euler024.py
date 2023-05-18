from tests.test_euler import TestEuler, TestEulerSetup
from euler024 import euler024

class TestEuler024(TestEulerSetup, TestEuler):
    problem_number = 24
    function = euler024
