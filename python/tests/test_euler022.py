from tests.test_euler import TestEuler, TestEulerSetup
from euler022 import euler022

class TestEuler022(TestEulerSetup, TestEuler):
    problem_number = 22
    function = euler022
