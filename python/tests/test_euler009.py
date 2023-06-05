from euler009 import euler009
from tests.test_euler import TestEuler, TestEulerSetup


class TestEuler009(TestEulerSetup, TestEuler):
    problem_number = 9
    function = euler009
