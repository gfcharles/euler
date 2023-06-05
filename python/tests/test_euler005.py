from euler005 import euler005
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler005(TestEulerSetup, TestEuler):
    problem_number = 5
    function = euler005
