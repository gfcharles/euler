from tests.test_euler import TestEuler, TestEulerSetup
from euler121 import euler121

class TestEuler121(TestEulerSetup, TestEuler):
    problem_number = 121
    function = euler121
