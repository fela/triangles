import unittest
from triangles import subsets, list_of_set_to_set_of_set


class TestListOfSetToSetOfSet(unittest.TestCase):

    def test_two(self):
        inp = [{1}, {}]
        output = {
            frozenset({1}),
            frozenset({})
        }
        self.assertEqual(list_of_set_to_set_of_set(inp), output)

    def test_empty(self):
        inp = list_of_set_to_set_of_set([])
        output = {}
        self.assertEqual(list_of_set_to_set_of_set(inp), output)

    def test_one(self):
        inp = list_of_set_to_set_of_set([{123}])
        output = {123}
        self.assertEqual(list_of_set_to_set_of_set(inp), output)


class TestSubset(unittest.TestCase):

    def test_empty(self):
        inp = {}
        output = {frozenset({})}
        self.assertEqual(subsets(inp), output)

    def test_one(self):
        inp = {1}
        output = {frozenset({1}), frozenset({})}
        self.assertEqual(subsets(inp), output)

    def test_two(self):
        inp = {1, 2}
        output = {
            frozenset({}),
            frozenset({1}),
            frozenset({2}),
            frozenset({1, 2})
        }
        self.assertEqual(subsets(inp), output)

    #def test_five(self):
    #    expected = {
    #        {},
    #        {1}, {2}, {3}, {4}, {5}
    #        {1, 2}, {1, 2}
    #    }
    #    self.assertEual(subsets({1, 2, 3, 4, 5}), {{}, {1}})

if __name__ == '__main__':
    unittest.main()