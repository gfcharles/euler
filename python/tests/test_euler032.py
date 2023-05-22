from tests.test_euler import TestEuler, TestEulerSetup
from euler032 import euler032

class TestEuler032(TestEulerSetup, TestEuler):
    problem_number = 32
    function = euler032
