"""
Python SDK for OpenFGA

API version: 1.x
Website: https://openfga.dev
Documentation: https://openfga.dev/docs
Support: https://openfga.dev/community
License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

from openfga_sdk.client.models.tuple import ClientTuple, convert_tuple_keys
from openfga_sdk.models.write_request_deletes import WriteRequestDeletes
from openfga_sdk.models.write_request_writes import WriteRequestWrites


class ClientWriteRequest:
    """
    ClientWriteRequest encapsulates the parameters required to write
    """

    def __init__(
        self, writes: list[ClientTuple] = None, deletes: list[ClientTuple] = None
    ):
        self._writes = writes
        self._deletes = deletes

    @property
    def writes(self):
        """
        Return writes
        """
        return self._writes

    @property
    def deletes(self):
        """
        Return deletes
        """
        return self._deletes

    @writes.setter
    def writes(self, value):
        """
        Set writes
        """
        self._writes = value

    @deletes.setter
    def deletes(self, value):
        """
        Set deletes
        """
        self._deletes = value

    @property
    def writes_tuple_keys(self):
        """
        Return the writes as tuple keys
        """
        keys = convert_tuple_keys(self.writes)
        if keys is None:
            return None
        return WriteRequestWrites(tuple_keys=keys)

    @property
    def deletes_tuple_keys(self):
        """
        Return the delete as tuple keys
        """
        keys = convert_tuple_keys(self.deletes)
        if keys is None:
            return None
        return WriteRequestDeletes(tuple_keys=keys)
