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


class ReadRequest(object):
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
        'authorization_model_id': 'str',
        'page_size': 'int',
        'continuation_token': 'str'
    }

    attribute_map = {
        'tuple_key': 'tuple_key',
        'authorization_model_id': 'authorization_model_id',
        'page_size': 'page_size',
        'continuation_token': 'continuation_token'
    }

    def __init__(self, tuple_key=None, authorization_model_id=None, page_size=None, continuation_token=None, local_vars_configuration=None):  # noqa: E501
        """ReadRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._tuple_key = None
        self._authorization_model_id = None
        self._page_size = None
        self._continuation_token = None
        self.discriminator = None

        if tuple_key is not None:
            self.tuple_key = tuple_key
        if authorization_model_id is not None:
            self.authorization_model_id = authorization_model_id
        if page_size is not None:
            self.page_size = page_size
        if continuation_token is not None:
            self.continuation_token = continuation_token

    @property
    def tuple_key(self):
        """Gets the tuple_key of this ReadRequest.  # noqa: E501


        :return: The tuple_key of this ReadRequest.  # noqa: E501
        :rtype: TupleKey
        """
        return self._tuple_key

    @tuple_key.setter
    def tuple_key(self, tuple_key):
        """Sets the tuple_key of this ReadRequest.


        :param tuple_key: The tuple_key of this ReadRequest.  # noqa: E501
        :type tuple_key: TupleKey
        """

        self._tuple_key = tuple_key

    @property
    def authorization_model_id(self):
        """Gets the authorization_model_id of this ReadRequest.  # noqa: E501


        :return: The authorization_model_id of this ReadRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorization_model_id

    @authorization_model_id.setter
    def authorization_model_id(self, authorization_model_id):
        """Sets the authorization_model_id of this ReadRequest.


        :param authorization_model_id: The authorization_model_id of this ReadRequest.  # noqa: E501
        :type authorization_model_id: str
        """

        self._authorization_model_id = authorization_model_id

    @property
    def page_size(self):
        """Gets the page_size of this ReadRequest.  # noqa: E501


        :return: The page_size of this ReadRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ReadRequest.


        :param page_size: The page_size of this ReadRequest.  # noqa: E501
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def continuation_token(self):
        """Gets the continuation_token of this ReadRequest.  # noqa: E501


        :return: The continuation_token of this ReadRequest.  # noqa: E501
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this ReadRequest.


        :param continuation_token: The continuation_token of this ReadRequest.  # noqa: E501
        :type continuation_token: str
        """

        self._continuation_token = continuation_token

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
        if not isinstance(other, ReadRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReadRequest):
            return True

        return self.to_dict() != other.to_dict()
