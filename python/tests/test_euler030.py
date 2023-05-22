from tests.test_euler import TestEuler, TestEulerSetup
from euler030 import euler030

class TestEuler030(TestEulerSetup, TestEuler):
    problem_number = 30
    function = euler030
