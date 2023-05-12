from test_euler_int import TestEulerInt
from euler011 import euler011

class TestEuler011(TestEulerInt):
    def __init__(self, *args):
        super().__init__(11, euler011, *args)
