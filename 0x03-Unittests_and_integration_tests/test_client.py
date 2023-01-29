#!/usr/bin/env python3
""" Test Client module. """
from client import GithubOrgClient
from unittest.mock import patch, Mock
from parameterized import parameterized
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test org """
        expected = {"name": org_name}
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        self.assertEqual(client.org, expected)
        expected_url = GithubOrgClient.ORG_URL.format(org=org_name)
        mock_get_json.assert_called_once_with(expected_url)
