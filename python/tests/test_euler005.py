from tests.test_euler import TestEuler, TestEulerSetup
from euler005 import euler005

class TestEuler005(TestEulerSetup, TestEuler):
    problem_number = 5
    function = euler005
