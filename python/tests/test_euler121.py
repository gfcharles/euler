from euler121 import euler121
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler121(TestEulerSetup, TestEuler):
    problem_number = 121
    function = euler121
