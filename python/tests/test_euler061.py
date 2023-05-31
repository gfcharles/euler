from tests.test_euler import TestEuler, TestEulerSetup
from euler061 import euler061

class TestEuler061(TestEulerSetup, TestEuler):
    problem_number = 61
    function = euler061
