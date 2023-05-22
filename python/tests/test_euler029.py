from tests.test_euler import TestEuler, TestEulerSetup
from euler029 import euler029

class TestEuler029(TestEulerSetup, TestEuler):
    problem_number = 29
    function = euler029
