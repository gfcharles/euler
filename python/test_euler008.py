from test_euler_int import TestEulerInt
from euler008 import euler008

class TestEuler008(TestEulerInt):
    def __init__(self, *args):
        super().__init__(8, euler008, *args)

