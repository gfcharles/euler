from tests.test_euler import TestEuler, TestEulerSetup
from euler025 import euler025

class TestEuler025(TestEulerSetup, TestEuler):
    problem_number = 25
    function = euler025
