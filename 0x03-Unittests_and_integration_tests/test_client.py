#!/usr/bin/env python3
""" Test Client module. """
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from requests import HTTPError
import unittest
import fixtures


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test has license """
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)


@parameterized_class([{
    "org_payload": fixture[0],
    "repos_payload": fixture[1],
    "expected_repos": fixture[2],
    "apache2_repos": fixture[3],
} for fixture in fixtures.TEST_PAYLOAD])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test Integration GithubOrgClient """
    @classmethod
    def setUpClass(cls):
        """ Set up class """
        config = {"json.return_value": cls.org_payload}
        cls.get_patcher = patch("requests.get", **config)
        cls.mock_get = cls.get_patcher.start()

        url_mapper = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload
        }

        def get_json(url):
            """ Mock implementation of get_json """
            return url_mapper.get(url, HTTPError)

        cls.get_json_patcher = patch("client.get_json", side_effect=get_json)
        cls.mock_get_json = cls.get_json_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        cls.get_patcher.stop()
        cls.get_json_patcher.stop()
