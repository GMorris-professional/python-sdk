# coding: utf-8

"""
   Python SDK for OpenFGA

   API version: 0.1
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://discord.gg/8naAwJfWN6
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""


import urllib3

from unittest import IsolatedAsyncioTestCase
from mock import patch
from datetime import datetime, timedelta
from openfga_sdk.sync.oauth2 import OAuth2Client
from openfga_sdk.sync import rest
from openfga_sdk.credentials import CredentialConfiguration, Credentials
from openfga_sdk.configuration import Configuration
from openfga_sdk.exceptions import AuthenticationError


# Helper function to construct mock response
def mock_response(body, status):
    headers = urllib3.response.HTTPHeaderDict({
        'content-type': 'application/json'
    })
    obj = urllib3.HTTPResponse(
        body,
        headers,
        status,
        preload_content=False
    )
    return rest.RESTResponse(obj, obj.data)


class TestOAuth2Client(IsolatedAsyncioTestCase):
    """TestOAuth2Client unit test"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_authentication_valid_client_credentials(self):
        """
        Test getting authentication header when method is client credentials
        """
        client = OAuth2Client(None)
        client._access_token = 'XYZ123'
        client._access_expiry_time = datetime.now() + timedelta(seconds=60)
        auth_header = client.get_authentication_header(None)
        self.assertEqual(auth_header, {'Authorization': 'Bearer XYZ123'})

    @patch.object(rest.RESTClientObject, 'request')
    def test_get_authentication_obtain_client_credentials(self, mock_request):
        """
        Test getting authentication header when method is client credential and we need to obtain token
        """
        response_body = '''
{
  "expires_in": 120,
  "access_token": "AABBCCDD"
}
        '''
        mock_request.return_value = mock_response(response_body, 200)

        credentials = Credentials(method="client_credentials",
                                  configuration=CredentialConfiguration(client_id='myclientid',
                                                                        client_secret='mysecret', api_issuer='www.testme.com', api_audience='myaudience'))
        rest_client = rest.RESTClientObject(Configuration())
        current_time = datetime.now()
        client = OAuth2Client(credentials)
        auth_header = client.get_authentication_header(rest_client)
        self.assertEqual(auth_header, {'Authorization': 'Bearer AABBCCDD'})
        self.assertEqual(client._access_token, 'AABBCCDD')
        self.assertGreaterEqual(client._access_expiry_time,
                                current_time + timedelta(seconds=int(120)))
        expected_header = urllib3.response.HTTPHeaderDict(
            {'Accept': 'application/json', 'Content-Type': 'application/json', 'User-Agent': 'openfga-sdk (python) 0.3.4'})
        mock_request.assert_called_once_with(
            'POST',
            'https://www.testme.com/oauth/token',
            headers=expected_header,
            query_params=None, post_params=None, _preload_content=True, _request_timeout=None,
            body={"client_id": "myclientid", "client_secret": "mysecret",
                  "audience": "myaudience", "grant_type": "client_credentials"}
        )
        rest_client.close()

    @patch.object(rest.RESTClientObject, 'request')
    def test_get_authentication_obtain_client_credentials_failed(self, mock_request):
        """
        Test getting authentication header when method is client credential and we fail to obtain token
        """
        response_body = '''
{
  "reason": "Unauthorized"
}
        '''
        mock_request.return_value = mock_response(response_body, 403)

        credentials = Credentials(method="client_credentials",
                                  configuration=CredentialConfiguration(client_id='myclientid',
                                                                        client_secret='mysecret', api_issuer='www.testme.com', api_audience='myaudience'))
        rest_client = rest.RESTClientObject(Configuration())
        client = OAuth2Client(credentials)
        with self.assertRaises(AuthenticationError):
            client.get_authentication_header(rest_client)
        rest_client.close()
