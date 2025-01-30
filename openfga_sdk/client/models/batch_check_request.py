"""
Python SDK for OpenFGA

API version: 1.x
Website: https://openfga.dev
Documentation: https://openfga.dev/docs
Support: https://openfga.dev/community
License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

from openfga_sdk.client.models.batch_check_item import ClientBatchCheckItem


class ClientBatchCheckRequest:
    """
    ClientBatchCheckRequest encapsulates the parameters for a BatchCheck request
    """

    def __init__(
        self,
        checks: list[ClientBatchCheckItem],
    ) -> None:
        self._checks = checks

    @property
    def checks(self) -> list[ClientBatchCheckItem]:
        """
        Return checks
        """
        return self._checks

    @checks.setter
    def checks(self, checks: list[ClientBatchCheckItem]) -> None:
        """
        Set checks
        """
        self._checks = checks
