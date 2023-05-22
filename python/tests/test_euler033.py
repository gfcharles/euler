from tests.test_euler import TestEuler, TestEulerSetup
from euler033 import euler033

class TestEuler033(TestEulerSetup, TestEuler):
    problem_number = 33
    function = euler033
