from tests.test_euler import TestEuler, TestEulerSetup
from euler035 import euler035

class TestEuler035(TestEulerSetup, TestEuler):
    problem_number = 35
    function = euler035
