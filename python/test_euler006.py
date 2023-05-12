from test_euler_int import TestEulerInt, TestEulerIntData
from euler006 import euler006

class TestEuler006(TestEulerInt):
    def __init__(self, *args):
        super().__init__(6, euler006, *args)
