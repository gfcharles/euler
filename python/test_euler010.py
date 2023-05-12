from test_euler_int import TestEulerInt
from euler010 import euler010

class TestEuler010(TestEulerInt):
    def __init__(self, *args):
        super().__init__(10, euler010, *args)
