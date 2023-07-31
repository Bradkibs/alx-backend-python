#!/usr/bin/env python3
""" Testing GithubOrgClient class in the client module"""


import unittest
from client import GithubOrgClient as GHOC
from unittest.mock import patch, MagicMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient class methods
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """
        Test TestGithubOrgClient's org method
        Args:
            org (str): organisation's name
        """
        org_test = GHOC(org)
        test_response = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()
