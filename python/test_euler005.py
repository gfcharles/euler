from test_euler_int import TestEulerInt, TestEulerIntData
from euler005 import euler005

class TestEuler005(TestEulerInt):
    def __init__(self, *args):
        super().__init__(5, euler005, *args)
