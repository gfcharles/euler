from unittest import TestCase
from euler004 import euler004

class TestEuler004(TestCase):
    def __init__(self, *args):
        super().__init__(4, euler004, *args)
