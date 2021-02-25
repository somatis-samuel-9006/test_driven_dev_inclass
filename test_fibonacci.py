import unittest
import fibonacci

class testFib(unittest.TestCase):
    def test0(self):
        self.assertEqual(fibonacci.fibonacci(0), 0)
        self.assertEqual(fibonacci.fibonacci(1), 1)
        self.assertEqual(fibonacci.fibonacci(4), 3)
        self.assertEqual(fibonacci.fibonacci(-1), "error")
    
    def test1(self):
        #pytest-like syntax
        assert(fibonacci.fibonacci(4) == 3)
        assert(fibonacci.fibonacci(0) == 0)
    
    def test2(self):
        assert(fibonacci.factorial(2) == 2)
        assert(fibonacci.factorial(6) == 720)
        assert(fibonacci.factorial(0) == 1)
        assert(fibonacci.factorial(-1) == "error")


if __name__ == '__main__':
    unittest.main()