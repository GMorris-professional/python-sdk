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


class StreamResultOfStreamedListObjectsResponse:
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
        "result": "StreamedListObjectsResponse",
        "error": "Status",
    }

    attribute_map: dict[str, str] = {"result": "result", "error": "error"}

    def __init__(self, result=None, error=None, local_vars_configuration=None):
        """StreamResultOfStreamedListObjectsResponse - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._error = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if error is not None:
            self.error = error

    @property
    def result(self):
        """Gets the result of this StreamResultOfStreamedListObjectsResponse.


        :return: The result of this StreamResultOfStreamedListObjectsResponse.
        :rtype: StreamedListObjectsResponse
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this StreamResultOfStreamedListObjectsResponse.


        :param result: The result of this StreamResultOfStreamedListObjectsResponse.
        :type result: StreamedListObjectsResponse
        """

        self._result = result

    @property
    def error(self):
        """Gets the error of this StreamResultOfStreamedListObjectsResponse.


        :return: The error of this StreamResultOfStreamedListObjectsResponse.
        :rtype: Status
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this StreamResultOfStreamedListObjectsResponse.


        :param error: The error of this StreamResultOfStreamedListObjectsResponse.
        :type error: Status
        """

        self._error = error

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
        if not isinstance(other, StreamResultOfStreamedListObjectsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StreamResultOfStreamedListObjectsResponse):
            return True

        return self.to_dict() != other.to_dict()
