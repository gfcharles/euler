from config.test_euler import TestEuler, TestEulerSetup
from euler010 import euler010

class TestEuler010(TestEulerSetup, TestEuler):
    problem_number = 10
    function = euler010
