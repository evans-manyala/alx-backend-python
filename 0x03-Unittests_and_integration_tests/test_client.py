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
        """
        Test that _public_repos_url
        returns the correct URL.
        """
        test_payload = {"repos_url":
                        "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = test_payload

        client = GithubOrgClient("google")
        result = client._public_repos_url

        self.assertEqual(result, test_payload["repos_url"])
        mock_org.assert_called_once()

    @patch("client.GithubOrgClient.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Test that GithubOrgClient.public_repos
        returns the correct list of repos.
        """
        test_payload = [{"name": "repo1"},
                        {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )

            client = GithubOrgClient("google")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )


if __name__ == "__main__":
    unittest.main()
