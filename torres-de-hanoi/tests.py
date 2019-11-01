from app import Hanoi
import unittest

class TestHanoi(unittest.TestCase):

    def test_hanoi(self):
        hanoi = Hanoi()
        self.assertEqual(hanoi.organizar(), 1)
        self.assertEqual(quantidadeDeMovimentos, hanoi.quantidadeDeMovimentos())

if __name__ == '__main__':
    unittest.main()