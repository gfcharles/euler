from euler025 import euler025
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler025(TestEulerSetup, TestEuler):
    problem_number = 25
    function = euler025
