import random
import unittest

from triangles import subsets

class TestSubset(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_empty(self):
        self.assertEqual(subsets({}), {{}})

    def test_one(self):
        self.assertEqual(subsets({1}), {{1}, {}})

    def test_two(self):
        self.assertEqual(subsets({1, 2}), {{}, {1}, {2}, {1, 2}})
        
    #def test_five(self):
    #    expected = {
    #        {},
    #        {1}, {2}, {3}, {4}, {5}
    #        {1, 2}, {1, 2}
    #    }
    #    self.assertEual(subsets({1, 2, 3, 4, 5}), {{}, {1}})

if __name__ == '__main__':
    unittest.main()