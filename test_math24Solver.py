from unittest import TestCase

from Math24 import Math24Solver


class TestMath24Solver(TestCase):
    def test__calculateEquation(self):
        self.assertEqual(Math24Solver._calculateEquation(self,2,"+",3),5)


