from tests.test_euler import TestEuler, TestEulerSetup
from euler060 import euler060

class TestEuler060(TestEulerSetup, TestEuler):
    problem_number = 60
    function = euler060
