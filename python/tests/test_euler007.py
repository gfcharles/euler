from tests.test_euler import TestEuler, TestEulerSetup
from euler007 import euler007

class TestEuler007(TestEulerSetup, TestEuler):
    problem_number = 7
    function = euler007
