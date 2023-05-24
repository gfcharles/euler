from tests.test_euler import TestEuler, TestEulerSetup
from euler081 import euler081

class TestEuler081(TestEulerSetup, TestEuler):
    problem_number = 81
    function = euler081
