import unittest
from vector import Vector

class testVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)


    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_minus(self):
        v = self.v1-self.v1
        self.assertEqual(getattr(v, 'x'), 0)

    def test_add(self):
        v = self.v1+self.v1
        self.assertEqual(getattr(v, 'x'), 2)

    def test_mul(self):
        v = self.v1*1
        self.assertEqual(getattr(v, 'x'), 1)

    def test_rmul(self):
        v = 1*self.v1
        self.assertEqual(getattr(v, 'x'), 1)


if __name__ == '__main__':
    unittest.main()
