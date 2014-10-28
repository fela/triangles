import random
import unittest

from triangles import subsets, list_of_set_to_set_of_set


class TestListOfSetToSetOfSet(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_two(self):
        self.assertEqual(list_of_set_to_set_of_set([{1}, {}]),
                         {frozenset({}), frozenset({1})})
        #    self.assertEual(subsets({1, 2, 3, 4, 5}), {{}, {1}})
        

class TestSubset(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_empty(self):
        self.assertEqual(subsets({}), {frozenset({})})

    def test_one(self):
        self.assertEqual(subsets({1}), {frozenset({1}), frozenset({})})

    def test_two(self):
        self.assertEqual(subsets({1, 2}), {frozenset({}), frozenset({1}),
                                           frozenset({2}), frozenset({1, 2})})

    #def test_five(self):
    #    expected = {
    #        {},
    #        {1}, {2}, {3}, {4}, {5}
    #        {1, 2}, {1, 2}
    #    }
    #    self.assertEual(subsets({1, 2, 3, 4, 5}), {{}, {1}})

if __name__ == '__main__':
    unittest.main()