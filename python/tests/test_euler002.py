from tests.test_euler import TestEuler, TestEulerSetup
from euler002 import euler002

class TestEuler002(TestEulerSetup, TestEuler):
    problem_number = 2
    function = euler002
