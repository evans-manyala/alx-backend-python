#!/usr/bin/env python3
"""
Testing the client module.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    @patch("client.GithubOrgClient.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        expected_org = {"login": org_name}
        mock_get_json.return_value = expected_org

        client = GithubOrgClient(org_name)
        result = client.get_org()

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_org)


if __name__ == "__main__":
    unittest.main()