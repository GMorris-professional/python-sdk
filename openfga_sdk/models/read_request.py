"""
   Python SDK for OpenFGA

   API version: 1.x
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://openfga.dev/community
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint

from openfga_sdk.configuration import Configuration


class ReadRequest:
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
        "tuple_key": "ReadRequestTupleKey",
        "page_size": "int",
        "continuation_token": "str",
        "consistency": "ConsistencyPreference",
    }

    attribute_map = {
        "tuple_key": "tuple_key",
        "page_size": "page_size",
        "continuation_token": "continuation_token",
        "consistency": "consistency",
    }

    def __init__(
        self,
        tuple_key=None,
        page_size=None,
        continuation_token=None,
        consistency=None,
        local_vars_configuration=None,
    ):
        """ReadRequest - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._tuple_key = None
        self._page_size = None
        self._continuation_token = None
        self._consistency = None
        self.discriminator = None

        if tuple_key is not None:
            self.tuple_key = tuple_key
        if page_size is not None:
            self.page_size = page_size
        if continuation_token is not None:
            self.continuation_token = continuation_token
        if consistency is not None:
            self.consistency = consistency

    @property
    def tuple_key(self):
        """Gets the tuple_key of this ReadRequest.


        :return: The tuple_key of this ReadRequest.
        :rtype: ReadRequestTupleKey
        """
        return self._tuple_key

    @tuple_key.setter
    def tuple_key(self, tuple_key):
        """Sets the tuple_key of this ReadRequest.


        :param tuple_key: The tuple_key of this ReadRequest.
        :type tuple_key: ReadRequestTupleKey
        """

        self._tuple_key = tuple_key

    @property
    def page_size(self):
        """Gets the page_size of this ReadRequest.


        :return: The page_size of this ReadRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ReadRequest.


        :param page_size: The page_size of this ReadRequest.
        :type page_size: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and page_size is not None
            and page_size > 100
        ):
            raise ValueError(
                "Invalid value for `page_size`, must be a value less than or equal to `100`"
            )
        if (
            self.local_vars_configuration.client_side_validation
            and page_size is not None
            and page_size < 1
        ):
            raise ValueError(
                "Invalid value for `page_size`, must be a value greater than or equal to `1`"
            )

        self._page_size = page_size

    @property
    def continuation_token(self):
        """Gets the continuation_token of this ReadRequest.


        :return: The continuation_token of this ReadRequest.
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this ReadRequest.


        :param continuation_token: The continuation_token of this ReadRequest.
        :type continuation_token: str
        """

        self._continuation_token = continuation_token

    @property
    def consistency(self):
        """Gets the consistency of this ReadRequest.


        :return: The consistency of this ReadRequest.
        :rtype: ConsistencyPreference
        """
        return self._consistency

    @consistency.setter
    def consistency(self, consistency):
        """Sets the consistency of this ReadRequest.


        :param consistency: The consistency of this ReadRequest.
        :type consistency: ConsistencyPreference
        """

        self._consistency = consistency

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
        if not isinstance(other, ReadRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReadRequest):
            return True

        return self.to_dict() != other.to_dict()
