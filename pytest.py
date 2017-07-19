import unittest
from hello import print_hello

class TestHello(unittest.TestCase):

    def test_hello(self):
        self.assertTrue(print_hello()=='hello')

if __name__=='__main__':
    unittest.main()
