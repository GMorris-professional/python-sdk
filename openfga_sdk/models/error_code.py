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


class ErrorCode:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NO_ERROR = "no_error"
    VALIDATION_ERROR = "validation_error"
    AUTHORIZATION_MODEL_NOT_FOUND = "authorization_model_not_found"
    AUTHORIZATION_MODEL_RESOLUTION_TOO_COMPLEX = (
        "authorization_model_resolution_too_complex"
    )
    INVALID_WRITE_INPUT = "invalid_write_input"
    CANNOT_ALLOW_DUPLICATE_TUPLES_IN_ONE_REQUEST = (
        "cannot_allow_duplicate_tuples_in_one_request"
    )
    CANNOT_ALLOW_DUPLICATE_TYPES_IN_ONE_REQUEST = (
        "cannot_allow_duplicate_types_in_one_request"
    )
    CANNOT_ALLOW_MULTIPLE_REFERENCES_TO_ONE_RELATION = (
        "cannot_allow_multiple_references_to_one_relation"
    )
    INVALID_CONTINUATION_TOKEN = "invalid_continuation_token"
    INVALID_TUPLE_SET = "invalid_tuple_set"
    INVALID_CHECK_INPUT = "invalid_check_input"
    INVALID_EXPAND_INPUT = "invalid_expand_input"
    UNSUPPORTED_USER_SET = "unsupported_user_set"
    INVALID_OBJECT_FORMAT = "invalid_object_format"
    WRITE_FAILED_DUE_TO_INVALID_INPUT = "write_failed_due_to_invalid_input"
    AUTHORIZATION_MODEL_ASSERTIONS_NOT_FOUND = (
        "authorization_model_assertions_not_found"
    )
    LATEST_AUTHORIZATION_MODEL_NOT_FOUND = "latest_authorization_model_not_found"
    TYPE_NOT_FOUND = "type_not_found"
    RELATION_NOT_FOUND = "relation_not_found"
    EMPTY_RELATION_DEFINITION = "empty_relation_definition"
    INVALID_USER = "invalid_user"
    INVALID_TUPLE = "invalid_tuple"
    UNKNOWN_RELATION = "unknown_relation"
    STORE_ID_INVALID_LENGTH = "store_id_invalid_length"
    ASSERTIONS_TOO_MANY_ITEMS = "assertions_too_many_items"
    ID_TOO_LONG = "id_too_long"
    AUTHORIZATION_MODEL_ID_TOO_LONG = "authorization_model_id_too_long"
    TUPLE_KEY_VALUE_NOT_SPECIFIED = "tuple_key_value_not_specified"
    TUPLE_KEYS_TOO_MANY_OR_TOO_FEW_ITEMS = "tuple_keys_too_many_or_too_few_items"
    PAGE_SIZE_INVALID = "page_size_invalid"
    PARAM_MISSING_VALUE = "param_missing_value"
    DIFFERENCE_BASE_MISSING_VALUE = "difference_base_missing_value"
    SUBTRACT_BASE_MISSING_VALUE = "subtract_base_missing_value"
    OBJECT_TOO_LONG = "object_too_long"
    RELATION_TOO_LONG = "relation_too_long"
    TYPE_DEFINITIONS_TOO_FEW_ITEMS = "type_definitions_too_few_items"
    TYPE_INVALID_LENGTH = "type_invalid_length"
    TYPE_INVALID_PATTERN = "type_invalid_pattern"
    RELATIONS_TOO_FEW_ITEMS = "relations_too_few_items"
    RELATIONS_TOO_LONG = "relations_too_long"
    RELATIONS_INVALID_PATTERN = "relations_invalid_pattern"
    OBJECT_INVALID_PATTERN = "object_invalid_pattern"
    QUERY_STRING_TYPE_CONTINUATION_TOKEN_MISMATCH = (
        "query_string_type_continuation_token_mismatch"
    )
    EXCEEDED_ENTITY_LIMIT = "exceeded_entity_limit"
    INVALID_CONTEXTUAL_TUPLE = "invalid_contextual_tuple"
    DUPLICATE_CONTEXTUAL_TUPLE = "duplicate_contextual_tuple"
    INVALID_AUTHORIZATION_MODEL = "invalid_authorization_model"
    UNSUPPORTED_SCHEMA_VERSION = "unsupported_schema_version"
    CANCELLED = "cancelled"
    INVALID_START_TIME = "invalid_start_time"

    allowable_values = [
        NO_ERROR,
        VALIDATION_ERROR,
        AUTHORIZATION_MODEL_NOT_FOUND,
        AUTHORIZATION_MODEL_RESOLUTION_TOO_COMPLEX,
        INVALID_WRITE_INPUT,
        CANNOT_ALLOW_DUPLICATE_TUPLES_IN_ONE_REQUEST,
        CANNOT_ALLOW_DUPLICATE_TYPES_IN_ONE_REQUEST,
        CANNOT_ALLOW_MULTIPLE_REFERENCES_TO_ONE_RELATION,
        INVALID_CONTINUATION_TOKEN,
        INVALID_TUPLE_SET,
        INVALID_CHECK_INPUT,
        INVALID_EXPAND_INPUT,
        UNSUPPORTED_USER_SET,
        INVALID_OBJECT_FORMAT,
        WRITE_FAILED_DUE_TO_INVALID_INPUT,
        AUTHORIZATION_MODEL_ASSERTIONS_NOT_FOUND,
        LATEST_AUTHORIZATION_MODEL_NOT_FOUND,
        TYPE_NOT_FOUND,
        RELATION_NOT_FOUND,
        EMPTY_RELATION_DEFINITION,
        INVALID_USER,
        INVALID_TUPLE,
        UNKNOWN_RELATION,
        STORE_ID_INVALID_LENGTH,
        ASSERTIONS_TOO_MANY_ITEMS,
        ID_TOO_LONG,
        AUTHORIZATION_MODEL_ID_TOO_LONG,
        TUPLE_KEY_VALUE_NOT_SPECIFIED,
        TUPLE_KEYS_TOO_MANY_OR_TOO_FEW_ITEMS,
        PAGE_SIZE_INVALID,
        PARAM_MISSING_VALUE,
        DIFFERENCE_BASE_MISSING_VALUE,
        SUBTRACT_BASE_MISSING_VALUE,
        OBJECT_TOO_LONG,
        RELATION_TOO_LONG,
        TYPE_DEFINITIONS_TOO_FEW_ITEMS,
        TYPE_INVALID_LENGTH,
        TYPE_INVALID_PATTERN,
        RELATIONS_TOO_FEW_ITEMS,
        RELATIONS_TOO_LONG,
        RELATIONS_INVALID_PATTERN,
        OBJECT_INVALID_PATTERN,
        QUERY_STRING_TYPE_CONTINUATION_TOKEN_MISMATCH,
        EXCEEDED_ENTITY_LIMIT,
        INVALID_CONTEXTUAL_TUPLE,
        DUPLICATE_CONTEXTUAL_TUPLE,
        INVALID_AUTHORIZATION_MODEL,
        UNSUPPORTED_SCHEMA_VERSION,
        CANCELLED,
        INVALID_START_TIME,
    ]

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types: dict[str, str] = {}

    attribute_map: dict[str, str] = {}

    def __init__(self, local_vars_configuration=None):
        """ErrorCode - a model defined in OpenAPI"""
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, ErrorCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorCode):
            return True

        return self.to_dict() != other.to_dict()
