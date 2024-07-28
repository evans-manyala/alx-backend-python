#!/usr/bin/env python3
"""
Funtion to test utils.py
"""
from typing import Self
import unittest
from parameterized import parameterized
from utils import access_nested_map, memoize, get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        from utils import access_nested_map

        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        with patch("utils.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


class TestMemoize(unittest.TestCase):

    def test_memoize(self) -> None:

        class TestClass:

            def a_method(self):
                return 42

        @memoize
        def a_property(self):
            return self.a_method()

        test_instance = unittest.TestCase()
        with patch.object(unittest.TestCase, "a_method") as mock:
            mock.return_value = 42

            result1 = test_instance.a_property()
            result2 = test_instance.a_property()
            Self.assertEqual(result1, 42)
            Self.assertEqual(result2, 42)
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
