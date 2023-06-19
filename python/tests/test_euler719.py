from tests.test_euler import TestEuler, TestEulerSetup
from euler719 import euler719


class TestEuler719(TestEulerSetup, TestEuler):
    problem_number = 719
    function = euler719
