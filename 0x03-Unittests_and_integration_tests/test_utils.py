#!/usr/bin/env python3
""" Test utils module. """
from utils import *
from parameterized import parameterized
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ("a", ), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test access_nested_map function exception. """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), expected)


class TestGetJson(unittest.TestCase):
    """ Test get_json function. """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test get_json function. """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)

    @patch("requests.get")
    def test_get_json_exception(self, mock_get):
        """ Test get_json function exception. """
        mock_get.side_effect = Exception("Not found")
        with self.assertRaises(Exception) as e:
            get_json("http://example.com")
        self.assertEqual(str(e.exception), "Not found")


class TestMemoize(unittest.TestCase):
    """ Test memoize function. """

    def test_memoize(self):
        """ Test memoize function. """
        class TestClass:
            """ Test class."""

            def a_method(self):
                """ Test method. """
                return 42

            @memoize
            def a_property(self):
                """ Test property. """
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mock_method:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)

        mock_method.assert_called_once()
