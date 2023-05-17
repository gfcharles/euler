from config.test_euler import TestEuler, TestEulerSetup
from euler018 import euler018

class TestEuler018(TestEulerSetup, TestEuler):
    problem_number = 18
    function = euler018
