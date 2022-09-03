import unittest
import sprints

class TestMyFunc(unittest.TestCase):
    def test_empty_list(self):
        """
        Test output of an empty list.
        Output should be (0, 0)
        """
        data = []
        expected = (0, 0)
        actual = sprints.MyFunc(data)
        self.assertEqual(actual, expected)


    def test_list_of_evens(self):
        """
        Test output of a list of odd numbers.
        List: [1, 3, 5, 7, 9]
        Output should be (0, 0)
        """
        data = [1, 3, 5, 7, 9]
        expected = (0, 0)
        actual = sprints.MyFunc(data)
        self.assertEqual(actual, expected)


    def test_list_of_evens(self):
        """
        Test output of a list of even numbers.
        List: [0, 2, 4, 6, 8, 10]
        Output should be (5.0, 0)
        """
        data = [0, 2, 4, 6, 8, 10]
        expected = (5.0, 0)
        actual = sprints.MyFunc(data)
        self.assertEqual(actual, expected)


    def test_list_of_floats(self):
        """
        Test output of a list of floats.
        List: [-1.0, 0.0, 1.0, 2.5]
        Output should be (0, 2.5)
        """
        data = [-1.0, 0.0, 1.0, 2.5]
        expected = (0, 2.5)
        actual = sprints.MyFunc(data)
        self.assertEqual(actual, expected)


    def test_mixed_list_zero(self):
        """
        Test output of a list of mixed list with neither
        integers nor floats.
        List: [1, True, False, 'test']
        Output should be (0, 0)
        """
        data = [1, True, False, 'test']
        expected = (0, 0)
        actual = sprints.MyFunc(data)
        self.assertEqual(actual, expected)


    def test_mixed_list_real(self):
        """
        Test output of a list of mixed list with neither
        integers nor floats.
        List: [1, 1.0, 2, 0, True, 10, False, -0.3, 15, 0, 0.0, 'test']
        Output should be (3.0, 1.0)
        """
        data = [1, 1.0, 2, 0, True, 10, False, -0.3, 15, 0, 0.0, 'test']
        expected = (3.0, 1.0)
        actual = sprints.MyFunc(data)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
