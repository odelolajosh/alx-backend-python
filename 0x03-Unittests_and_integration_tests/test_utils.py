#!/usr/bin/env python3
""" Test utils module. """
from utils import *
from parameterized import parameterized
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ Test access_nested_map function. """

    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map function. """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self):
        """ Test access_nested_map function exception. """
        nested_map = {"a": 1}
        path = ["a", "b"]
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), "'b'")
