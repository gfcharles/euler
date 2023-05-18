from tests.test_euler import TestEuler, TestEulerSetup
from euler023 import euler023

class TestEuler023(TestEulerSetup, TestEuler):
    problem_number = 23
    function = euler023
