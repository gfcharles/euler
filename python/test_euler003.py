from euler003 import euler003
from test_euler_int import TestEulerInt


class TestEuler003(TestEulerInt):
    def __init__(self, *args):
        super().__init__(3, euler003, *args)
