from euler021 import euler021
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler021(TestEulerSetup, TestEuler):
    problem_number = 21
    function = euler021
