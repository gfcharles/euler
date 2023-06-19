from tests.test_euler import TestEuler, TestEulerSetup
from euler099 import euler099


class TestEuler099(TestEulerSetup, TestEuler):
    problem_number = 99
    function = euler099
