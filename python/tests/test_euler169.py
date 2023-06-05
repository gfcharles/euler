from tests.test_euler import TestEuler, TestEulerSetup
from euler169 import euler169


class TestEuler169(TestEulerSetup, TestEuler):
    problem_number = 169
    function = euler169
