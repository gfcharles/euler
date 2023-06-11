from tests.test_euler import TestEuler, TestEulerSetup
from euler097 import euler097


class TestEuler097(TestEulerSetup, TestEuler):
    problem_number = 97
    function = euler097
