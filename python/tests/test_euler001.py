from tests.test_euler import TestEuler, TestEulerSetup
from euler001 import euler001

class TestEuler001(TestEulerSetup, TestEuler):
    problem_number = 1
    function = euler001
