from tests.test_euler import TestEuler, TestEulerSetup
from euler065 import euler065


class TestEuler065(TestEulerSetup, TestEuler):
    problem_number = 65
    function = euler065
