from tests.test_euler import TestEuler, TestEulerSetup
from euler064 import euler064


class TestEuler064(TestEulerSetup, TestEuler):
    problem_number = 64
    function = euler064
