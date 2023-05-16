from test_euler_int import TestEuler, TestEulerIntData
from euler007 import euler007

class TestEuler007(TestEulerInt):
    def __init__(self, *args):
        super().__init__(7, euler007, *args)
