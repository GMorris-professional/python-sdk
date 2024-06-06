"""
   Python SDK for OpenFGA

   API version: 1.x
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://openfga.dev/community
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

from openfga_sdk.configuration import Configuration
from openfga_sdk.exceptions import FgaValidationException
from openfga_sdk.validation import is_well_formed_ulid_string


class ClientConfiguration(Configuration):
    """
    OpenFGA client configuration
    """

    def __init__(
        self,
        api_scheme="https",
        api_host=None,
        store_id=None,
        credentials=None,
        retry_params=None,
        authorization_model_id=None,
        ssl_ca_cert=None,
        api_url=None,  # TODO: restructure when removing api_scheme/api_host
    ):
        super().__init__(
            api_scheme,
            api_host,
            store_id,
            credentials,
            retry_params,
            ssl_ca_cert=ssl_ca_cert,
            api_url=api_url,
        )
        self._authorization_model_id = authorization_model_id

    def is_valid(self):
        super().is_valid()

        if (
            self.authorization_model_id is not None
            and self.authorization_model_id != ""
            and is_well_formed_ulid_string(self.authorization_model_id) is False
        ):
            raise FgaValidationException(
                "authorization_model_id ('%s') is not in a valid ulid format"
                % self.authorization_model_id
            )

    @property
    def authorization_model_id(self):
        return self._authorization_model_id

    @authorization_model_id.setter
    def authorization_model_id(self, value):
        self._authorization_model_id = value
