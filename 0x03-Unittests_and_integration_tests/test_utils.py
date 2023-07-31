#!/usr/bin/env python3
"""Unittest for access_nested_map function of utils module"""


from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """A unittest for the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_access_nested_map(self, nested_map, path, answer):
        """testing function"""
        self.assertEqual(access_nested_map(nested_map, path), answer)
