from app import hanoi
import unittest

class TestHanoi(unittest.TestCase):

    def test_hanoi(self):
        self.assertEqual(hanoi(1), 1)

if __name__ == '__main__':
    unittest.main()