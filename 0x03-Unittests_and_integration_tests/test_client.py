#!/usr/bin/env python3
"""
Testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch(
        "client.GithubOrgClient.get_json",
    )
    def test_org(
        self, org_name: str, expected_org: Dict, mock_get_json: MagicMock
    ) -> None:
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = expected_org

        client = GithubOrgClient(org_name)
        result = client.org()

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_org)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org: PropertyMock) -> None:
        """Test that _public_repos_url returns the correct URL."""
        test_payload = {"repos_url":
                        "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = test_payload

        client = GithubOrgClient("google")
        result = client._public_repos_url

        self.assertEqual(result, test_payload["repos_url"])
        mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
