import unittest
from unittest.mock import MagicMock

import application as app
"""
Unit tests
Must start with 'test_'
Must import unittest
Must have (self) in method declaration
Ideally each test will test 1 thing (have one assertion)
"""


class AppTest(unittest.TestCase):

    def test_simple_max_num(self):
        """ Tests the max_num function """
        x = 1
        y = 10
        res = app.num_max(1, 10)
        self.assertEqual(res, 10)

    def test_max_with_no_numbers(self):
        """ Tests with bad values. Expecting TypeError
        Ideally, we would handle exceptions in the program
        """
        with self.assertRaises(TypeError):
            app.num_max("text", 15)

    def test_num_max_with_none(self):
        """ Tests that passing in a None type results in a TypeError"""
        with self.assertRaises(TypeError):
            app.num_max(1, None)

    def test_array_max_good(self):
        """ Tests that the expected value comes from array_max """
        test = [1, 5, 2, 6, 2, 9, 1]
        res = app.array_max(test)
        self.assertEqual(res, 9)

    def test_array_wrong_type(self):
        """ Asserts a type error when using a Set """
        test = {1, 5, 2, 6, 2, 9, 1}
        '''Set don't support indexing'''
        with self.assertRaises(TypeError):
            app.array_max(test)

    def test_array_max_null_value(self):
        """ Asserts a type error when using a None value """
        test = None
        with self.assertRaises(TypeError):
            app.array_max(test)

    def test_is_valid(self):
        """ Tests for expected results from is_valid"""
        credentials = "test"
        self.assertTrue(app.is_valid(credentials))
        self.assertFalse(app.is_valid("bad credentials"))

    def test_current_data(self):
        """ Tests the expected keys are returned """
        expected_keys = {'gps', 'time', 'temp', 'leaf wetness', 'humidity'}
        res = app.get_data()
        data = res['data']
        error = res['errors']
        self.assertSetEqual(set(data), expected_keys)
        self.assertEqual(error, None)

    def test_data_types(self):
        """ When you don't know what values might be, can check types"""
        res = app.get_data()
        data = res['data']
        self.assertIsInstance(data['gps'], tuple)
        self.assertIsInstance(data['gps'][0], float)
        self.assertIsInstance(data['gps'][0], float)

        self.assertIsInstance(data['time'], float)
        self.assertIsInstance(data['temp'], float)
        self.assertIsInstance(data['leaf wetness'], float)
        self.assertIsInstance(data['humidity'], float)

    def test_failed_get_data(self):
        """ Using Mocks to cause a function in another module to throw an exception.
        Here, app.get_app calls app.current_data. This mock will cause app.current_data to throw an Exception. """
        app.current_data = MagicMock(side_effect=Exception("Connection Failed!"))
        res = app.get_data()
        data = res['data']
        error = res['errors']
        self.assertEqual(data, None)
        self.assertEqual(error, "Connection Failed!")


if __name__ == '__main__':
    unittest.main()