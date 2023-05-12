from euler002 import euler002
from test_euler_int import TestEulerInt


class TestEuler002(TestEulerInt):
    def __init__(self, *args):
        super().__init__(2, euler002, *args)
