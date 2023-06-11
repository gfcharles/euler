from tests.test_euler import TestEuler, TestEulerSetup
from euler068 import euler068


class TestEuler068(TestEulerSetup, TestEuler):
    problem_number = 68
    function = euler068
