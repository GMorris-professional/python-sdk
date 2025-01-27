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


class CheckError:
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
        "input_error": "ErrorCode",
        "internal_error": "InternalErrorCode",
        "message": "str",
    }

    attribute_map = {
        "input_error": "input_error",
        "internal_error": "internal_error",
        "message": "message",
    }

    def __init__(
        self,
        input_error=None,
        internal_error=None,
        message=None,
        local_vars_configuration=None,
    ):
        """CheckError - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._input_error = None
        self._internal_error = None
        self._message = None
        self.discriminator = None

        if input_error is not None:
            self.input_error = input_error
        if internal_error is not None:
            self.internal_error = internal_error
        if message is not None:
            self.message = message

    @property
    def input_error(self):
        """Gets the input_error of this CheckError.


        :return: The input_error of this CheckError.
        :rtype: ErrorCode
        """
        return self._input_error

    @input_error.setter
    def input_error(self, input_error):
        """Sets the input_error of this CheckError.


        :param input_error: The input_error of this CheckError.
        :type input_error: ErrorCode
        """

        self._input_error = input_error

    @property
    def internal_error(self):
        """Gets the internal_error of this CheckError.


        :return: The internal_error of this CheckError.
        :rtype: InternalErrorCode
        """
        return self._internal_error

    @internal_error.setter
    def internal_error(self, internal_error):
        """Sets the internal_error of this CheckError.


        :param internal_error: The internal_error of this CheckError.
        :type internal_error: InternalErrorCode
        """

        self._internal_error = internal_error

    @property
    def message(self):
        """Gets the message of this CheckError.


        :return: The message of this CheckError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CheckError.


        :param message: The message of this CheckError.
        :type message: str
        """

        self._message = message

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
        if not isinstance(other, CheckError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CheckError):
            return True

        return self.to_dict() != other.to_dict()
