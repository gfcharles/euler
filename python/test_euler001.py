from euler001 import euler001
from test_euler_int import TestEulerInt


class TestEuler001(TestEulerInt):
    def __init__(self, *args):
        super().__init__(1, euler001, *args)
