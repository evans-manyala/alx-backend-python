#!/usr/bin/env python3
"""
Funtion to test utils.py
"""
import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        from utils import access_nested_map
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == "__main__":
    unittest.main()