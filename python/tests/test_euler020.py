from config.test_euler import TestEuler, TestEulerSetup
from euler020 import euler020

class TestEuler020(TestEulerSetup, TestEuler):
    problem_number = 20
    function = euler020
