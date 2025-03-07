"""
Python SDK for OpenFGA

API version: 1.x
Website: https://openfga.dev
Documentation: https://openfga.dev/docs
Support: https://openfga.dev/community
License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

import pprint

from inspect import getfullargspec

from openfga_sdk.configuration import Configuration


class BatchCheckItem:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types: dict[str, str] = {
        "tuple_key": "CheckRequestTupleKey",
        "contextual_tuples": "ContextualTupleKeys",
        "context": "object",
        "correlation_id": "str",
    }

    attribute_map: dict[str, str] = {
        "tuple_key": "tuple_key",
        "contextual_tuples": "contextual_tuples",
        "context": "context",
        "correlation_id": "correlation_id",
    }

    def __init__(
        self,
        tuple_key=None,
        contextual_tuples=None,
        context=None,
        correlation_id=None,
        local_vars_configuration=None,
    ):
        """BatchCheckItem - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._tuple_key = None
        self._contextual_tuples = None
        self._context = None
        self._correlation_id = None
        self.discriminator = None

        self.tuple_key = tuple_key
        if contextual_tuples is not None:
            self.contextual_tuples = contextual_tuples
        if context is not None:
            self.context = context
        self.correlation_id = correlation_id

    @property
    def tuple_key(self):
        """Gets the tuple_key of this BatchCheckItem.


        :return: The tuple_key of this BatchCheckItem.
        :rtype: CheckRequestTupleKey
        """
        return self._tuple_key

    @tuple_key.setter
    def tuple_key(self, tuple_key):
        """Sets the tuple_key of this BatchCheckItem.


        :param tuple_key: The tuple_key of this BatchCheckItem.
        :type tuple_key: CheckRequestTupleKey
        """
        if self.local_vars_configuration.client_side_validation and tuple_key is None:
            raise ValueError("Invalid value for `tuple_key`, must not be `None`")

        self._tuple_key = tuple_key

    @property
    def contextual_tuples(self):
        """Gets the contextual_tuples of this BatchCheckItem.


        :return: The contextual_tuples of this BatchCheckItem.
        :rtype: ContextualTupleKeys
        """
        return self._contextual_tuples

    @contextual_tuples.setter
    def contextual_tuples(self, contextual_tuples):
        """Sets the contextual_tuples of this BatchCheckItem.


        :param contextual_tuples: The contextual_tuples of this BatchCheckItem.
        :type contextual_tuples: ContextualTupleKeys
        """

        self._contextual_tuples = contextual_tuples

    @property
    def context(self):
        """Gets the context of this BatchCheckItem.


        :return: The context of this BatchCheckItem.
        :rtype: object
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this BatchCheckItem.


        :param context: The context of this BatchCheckItem.
        :type context: object
        """

        self._context = context

    @property
    def correlation_id(self):
        """Gets the correlation_id of this BatchCheckItem.

        correlation_id must be a string containing only letters, numbers, or hyphens, with length ≤ 36 characters.

        :return: The correlation_id of this BatchCheckItem.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this BatchCheckItem.

        correlation_id must be a string containing only letters, numbers, or hyphens, with length ≤ 36 characters.

        :param correlation_id: The correlation_id of this BatchCheckItem.
        :type correlation_id: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and correlation_id is None
        ):
            raise ValueError("Invalid value for `correlation_id`, must not be `None`")

        self._correlation_id = correlation_id

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(lambda item: (item[0], convert(item[1])), value.items())
                )
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchCheckItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchCheckItem):
            return True

        return self.to_dict() != other.to_dict()
