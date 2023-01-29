#!/usr/bin/env python3
""" Test Client module. """
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """ Test org """
        expected = {"name": org_name}
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        self.assertEqual(client.org, expected)
        expected_url = GithubOrgClient.ORG_URL.format(org=org_name)
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """ Test public repos url """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as org_property_mock:
            expected = {
                "repos_url": "https://api.github.com/orgs/google/repos"}
            org_property_mock.return_value = expected
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, expected["repos_url"])
            org_property_mock.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock: Mock):
        """ Test public repos """
        expected = ["alx-backend", "alx-backend-python"]
        get_json_mock.return_value = [{"name": repo} for repo in expected]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as public_repos_url_mock:
            test_url = "https://api.github.com/orgs/google/repos"
            public_repos_url_mock.return_value = test_url
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(),
                             ["alx-backend", "alx-backend-python"])
            get_json_mock.assert_called_once_with(test_url)
