from tests.test_euler import TestEuler, TestEulerSetup
from euler067 import euler067


class TestEuler067(TestEulerSetup, TestEuler):
    problem_number = 67
    function = euler067
