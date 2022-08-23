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

try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openfga_sdk.configuration import Configuration


class CheckRequest(object):
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
    openapi_types = {
        'tuple_key': 'TupleKey',
        'contextual_tuples': 'ContextualTupleKeys',
        'authorization_model_id': 'str',
        'trace': 'bool'
    }

    attribute_map = {
        'tuple_key': 'tuple_key',
        'contextual_tuples': 'contextual_tuples',
        'authorization_model_id': 'authorization_model_id',
        'trace': 'trace'
    }

    def __init__(self, tuple_key=None, contextual_tuples=None, authorization_model_id=None, trace=None, local_vars_configuration=None):  # noqa: E501
        """CheckRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._tuple_key = None
        self._contextual_tuples = None
        self._authorization_model_id = None
        self._trace = None
        self.discriminator = None

        if tuple_key is not None:
            self.tuple_key = tuple_key
        if contextual_tuples is not None:
            self.contextual_tuples = contextual_tuples
        if authorization_model_id is not None:
            self.authorization_model_id = authorization_model_id
        if trace is not None:
            self.trace = trace

    @property
    def tuple_key(self):
        """Gets the tuple_key of this CheckRequest.  # noqa: E501


        :return: The tuple_key of this CheckRequest.  # noqa: E501
        :rtype: TupleKey
        """
        return self._tuple_key

    @tuple_key.setter
    def tuple_key(self, tuple_key):
        """Sets the tuple_key of this CheckRequest.


        :param tuple_key: The tuple_key of this CheckRequest.  # noqa: E501
        :type tuple_key: TupleKey
        """

        self._tuple_key = tuple_key

    @property
    def contextual_tuples(self):
        """Gets the contextual_tuples of this CheckRequest.  # noqa: E501


        :return: The contextual_tuples of this CheckRequest.  # noqa: E501
        :rtype: ContextualTupleKeys
        """
        return self._contextual_tuples

    @contextual_tuples.setter
    def contextual_tuples(self, contextual_tuples):
        """Sets the contextual_tuples of this CheckRequest.


        :param contextual_tuples: The contextual_tuples of this CheckRequest.  # noqa: E501
        :type contextual_tuples: ContextualTupleKeys
        """

        self._contextual_tuples = contextual_tuples

    @property
    def authorization_model_id(self):
        """Gets the authorization_model_id of this CheckRequest.  # noqa: E501


        :return: The authorization_model_id of this CheckRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorization_model_id

    @authorization_model_id.setter
    def authorization_model_id(self, authorization_model_id):
        """Sets the authorization_model_id of this CheckRequest.


        :param authorization_model_id: The authorization_model_id of this CheckRequest.  # noqa: E501
        :type authorization_model_id: str
        """

        self._authorization_model_id = authorization_model_id

    @property
    def trace(self):
        """Gets the trace of this CheckRequest.  # noqa: E501

        Defaults to false. Making it true has performance implications.  # noqa: E501

        :return: The trace of this CheckRequest.  # noqa: E501
        :rtype: bool
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this CheckRequest.

        Defaults to false. Making it true has performance implications.  # noqa: E501

        :param trace: The trace of this CheckRequest.  # noqa: E501
        :type trace: bool
        """

        self._trace = trace

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

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
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
        if not isinstance(other, CheckRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CheckRequest):
            return True

        return self.to_dict() != other.to_dict()
