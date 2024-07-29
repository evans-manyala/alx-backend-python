#!/usr/bin/env python3
"""
Testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import (
    patch, Mock, MagicMock
)
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand(
        [
            ("google",{"login": "google"}),
            ("abc",{"login": "abc"}),
        ]
    )
    @patch("client.GithubOrgClient.get_json",)
    def test_org(self, org_name: str, expected_org: Dict, mock_get_json: MagicMock) -> None:
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = expected_org

        client = GithubOrgClient(org_name)
        result = client.org()

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_org)


if __name__ == "__main__":
    unittest.main()
