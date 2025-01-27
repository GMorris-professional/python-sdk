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


class ConditionParamTypeRef:
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
        "type_name": "TypeName",
        "generic_types": "list[ConditionParamTypeRef]",
    }

    attribute_map = {"type_name": "type_name", "generic_types": "generic_types"}

    def __init__(
        self, type_name=None, generic_types=None, local_vars_configuration=None
    ):
        """ConditionParamTypeRef - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type_name = None
        self._generic_types = None
        self.discriminator = None

        self.type_name = type_name
        if generic_types is not None:
            self.generic_types = generic_types

    @property
    def type_name(self):
        """Gets the type_name of this ConditionParamTypeRef.


        :return: The type_name of this ConditionParamTypeRef.
        :rtype: TypeName
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this ConditionParamTypeRef.


        :param type_name: The type_name of this ConditionParamTypeRef.
        :type type_name: TypeName
        """
        if self.local_vars_configuration.client_side_validation and type_name is None:
            raise ValueError("Invalid value for `type_name`, must not be `None`")

        self._type_name = type_name

    @property
    def generic_types(self):
        """Gets the generic_types of this ConditionParamTypeRef.


        :return: The generic_types of this ConditionParamTypeRef.
        :rtype: list[ConditionParamTypeRef]
        """
        return self._generic_types

    @generic_types.setter
    def generic_types(self, generic_types):
        """Sets the generic_types of this ConditionParamTypeRef.


        :param generic_types: The generic_types of this ConditionParamTypeRef.
        :type generic_types: list[ConditionParamTypeRef]
        """

        self._generic_types = generic_types

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
        if not isinstance(other, ConditionParamTypeRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConditionParamTypeRef):
            return True

        return self.to_dict() != other.to_dict()
