import unittest
from triangles import subsets, list_of_set_to_set_of_set


class TestListOfSetToSetOfSet(unittest.TestCase):

    def test_two(self):
        inp = [{1}, set()]
        output = {
            frozenset({1}),
            frozenset(set())
        }
        self.assertEqual(list_of_set_to_set_of_set(inp), output)

    def test_empty(self):
        inp = []
        output = set()
        self.assertEqual(list_of_set_to_set_of_set(inp), output)

    def test_one(self):
        inp = [{123}]
        output = {frozenset({123})}
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

    def test_four(self):
        """
        I'm using list_of_set_to_set_of_set so if that function does not
        run this test will be broken
        """
        inp = subsets({1, 2, 3, 4})
        output = list_of_set_to_set_of_set([
            {},
            {1}, {2}, {3}, {4},
            {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4},
            {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4},
            {1, 2, 3, 4}
        ])
        self.assertEqual(inp, output)

if __name__ == '__main__':
    unittest.main()