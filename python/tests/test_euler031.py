from tests.test_euler import TestEuler, TestEulerSetup
from euler031 import euler031

class TestEuler031(TestEulerSetup, TestEuler):
    problem_number = 31
    function = euler031
