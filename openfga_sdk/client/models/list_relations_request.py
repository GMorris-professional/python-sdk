"""
   Python SDK for OpenFGA

   API version: 1.x
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://openfga.dev/community
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

from openfga_sdk.client.models.tuple import ClientTuple


class ClientListRelationsRequest:
    """
    ClientListRelationsRequest encapsulates the parameters required for list all relations user have with object
    """

    def __init__(
        self,
        user: str,
        relations: list[str],
        object: str,
        contextual_tuples: list[ClientTuple] = None,
        context: object = None,
    ):
        self._user = user
        self._relations = relations
        self._object = object
        self._contextual_tuples = contextual_tuples
        self._context = context

    @property
    def user(self):
        """
        Return user
        """
        return self._user

    @property
    def relations(self):
        """
        Return relations
        """
        return self._relations

    @property
    def object(self):
        """
        Return object
        """
        return self._object

    @property
    def contextual_tuples(self):
        """
        Return contextual_tuples
        """
        return self._contextual_tuples

    @property
    def context(self):
        """
        Return context
        """
        return self._context

    @user.setter
    def user(self, value):
        """
        Set user
        """
        self._user = value

    @relations.setter
    def relations(self, value):
        """
        Set relations
        """
        self._relations = value

    @object.setter
    def object(self, value):
        """
        Set object
        """
        self._object = value

    @contextual_tuples.setter
    def contextual_tuples(self, value):
        """
        Set contextual tuples
        """
        self._contextual_tuples = value

    @context.setter
    def context(self, value):
        """
        Set context
        """
        self._context = value
