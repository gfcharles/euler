from config.test_euler import TestEuler, TestEulerSetup
from euler011 import euler011

class TestEuler011(TestEulerSetup, TestEuler):
    problem_number = 11
    function = euler011
