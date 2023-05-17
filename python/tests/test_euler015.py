from config.test_euler import TestEuler, TestEulerSetup
from euler015 import euler015

class TestEuler015(TestEulerSetup, TestEuler):
    problem_number = 15
    function = euler015
