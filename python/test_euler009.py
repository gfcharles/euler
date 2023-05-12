from test_euler_int import TestEulerInt
from euler009 import euler009

class TestEuler009(TestEulerInt):
    def __init__(self, *args):
        super().__init__(9, euler009, *args)
