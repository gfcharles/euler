from euler020 import euler020
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler020(TestEulerSetup, TestEuler):
    problem_number = 20
    function = euler020
