import unittest
from app import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, DevOps!")

if __name__ == "__main__":
    unittest.main()
