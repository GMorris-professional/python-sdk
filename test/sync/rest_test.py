"""
   Python SDK for OpenFGA

   API version: 1.x
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://openfga.dev/community
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

import json
from unittest.mock import MagicMock

import pytest

from openfga_sdk.exceptions import (
    ApiException,
    ForbiddenException,
    NotFoundException,
    RateLimitExceededError,
    ServiceException,
    UnauthorizedException,
    ValidationException,
)
from openfga_sdk.sync.rest import RESTClientObject, RESTResponse


def test_restresponse_init():
    mock_resp = MagicMock()
    mock_resp.status = 200
    mock_resp.reason = "OK"
    resp_data = b'{"test":"data"}'

    rest_resp = RESTResponse(mock_resp, resp_data)
    assert rest_resp.status == 200
    assert rest_resp.reason == "OK"
    assert rest_resp.data == resp_data
    assert rest_resp.urllib3_response == mock_resp


def test_restresponse_getheaders():
    mock_resp = MagicMock()
    mock_resp.headers = {"Content-Type": "application/json", "X-Testing": "true"}

    rest_resp = RESTResponse(mock_resp, b"")
    headers = rest_resp.getheaders()

    assert headers["Content-Type"] == "application/json"
    assert headers["X-Testing"] == "true"


def test_restresponse_getheader():
    mock_resp = MagicMock()
    mock_resp.headers = {"Content-Type": "application/json"}

    rest_resp = RESTResponse(mock_resp, b"")
    val = rest_resp.getheader("Content-Type")
    missing = rest_resp.getheader("X-Not-Here", default="fallback")

    assert val == "application/json"
    assert missing == "fallback"


def test_build_request_json_body():
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    req_args = client.build_request(
        method="POST",
        url="http://example.com/test",
        body={"foo": "bar"},
        headers={"Content-Type": "application/json"},
    )

    assert req_args["method"] == "POST"
    assert req_args["url"] == "http://example.com/test"
    assert req_args["headers"]["Content-Type"] == "application/json"
    assert json.loads(req_args["body"]) == {"foo": "bar"}


def test_build_request_multipart():
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    req_args = client.build_request(
        method="POST",
        url="http://example.com/upload",
        post_params={"file": ("filename.txt", b"contents", "text/plain")},
        headers={"Content-Type": "multipart/form-data"},
    )

    assert req_args["method"] == "POST"
    assert req_args["url"] == "http://example.com/upload"
    assert "Content-Type" not in req_args["headers"]
    assert req_args["encode_multipart"] is True
    assert req_args["fields"] == {"file": ("filename.txt", b"contents", "text/plain")}


def test_build_request_timeout():
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    req_args = client.build_request(
        method="GET",
        url="http://example.com",
        _request_timeout=10.0,
    )

    # We'll just confirm that the "timeout" object was set to 10.0
    # A deeper check might be verifying urllib3.Timeout, but this suffices.
    assert req_args["timeout"].total == 10.0


def test_handle_response_exception_success():
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    mock_response = MagicMock()
    mock_response.status = 200

    client.handle_response_exception(mock_response)  # no exception


@pytest.mark.parametrize(
    "status,exc",
    [
        (400, ValidationException),
        (401, UnauthorizedException),
        (403, ForbiddenException),
        (404, NotFoundException),
        (429, RateLimitExceededError),
        (500, ServiceException),
        (418, ApiException),
    ],
)
def test_handle_response_exception_error(status, exc):
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    mock_response = MagicMock()
    mock_response.status = status

    with pytest.raises(exc):
        client.handle_response_exception(mock_response)


def test_close():
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    mock_pool_manager = MagicMock()
    client.pool_manager = mock_pool_manager

    client.close()
    mock_pool_manager.clear.assert_called_once()


def test_request_preload_content():
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    mock_pool_manager = MagicMock()
    client.pool_manager = mock_pool_manager

    mock_raw_response = MagicMock()
    mock_raw_response.status = 200
    mock_raw_response.reason = "OK"
    mock_raw_response.data = b'{"some":"data"}'

    mock_pool_manager.request.return_value = mock_raw_response

    resp = client.request(method="GET", url="http://example.com", _preload_content=True)

    mock_pool_manager.request.assert_called_once()
    assert isinstance(resp, RESTResponse)
    assert resp.status == 200
    assert resp.data == b'{"some":"data"}'
    mock_pool_manager.clear.assert_called_once()


def test_request_no_preload_content():
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    mock_pool_manager = MagicMock()
    client.pool_manager = mock_pool_manager

    mock_raw_response = MagicMock()
    mock_raw_response.status = 200
    mock_raw_response.reason = "OK"
    mock_raw_response.data = b"unused"

    mock_pool_manager.request.return_value = mock_raw_response

    resp = client.request(
        method="GET", url="http://example.com", _preload_content=False
    )

    mock_pool_manager.request.assert_called_once()
    # We expect the raw HTTPResponse
    assert resp == mock_raw_response
    assert resp.status == 200
    mock_pool_manager.clear.assert_called_once()


def test_stream_happy_path():
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    mock_pool_manager = MagicMock()
    client.pool_manager = mock_pool_manager

    class FakeHTTPResponse:
        def __init__(self):
            self.status = 200
            self.reason = "OK"

        def stream(self, chunk_size):
            # Single chunk with two JSON lines
            yield b'{"foo":"bar"}\n{"hello":"world"}'

        def release_conn(self):
            pass

    mock_response = FakeHTTPResponse()
    mock_pool_manager.request.return_value = mock_response

    results = list(client.stream("GET", "http://example.com"))

    assert results == [{"foo": "bar"}, {"hello": "world"}]
    mock_pool_manager.request.assert_called_once()
    mock_pool_manager.clear.assert_called_once()


def test_stream_partial_chunks():
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    mock_pool_manager = MagicMock()
    client.pool_manager = mock_pool_manager

    class FakeHTTPResponse:
        def __init__(self):
            self.status = 200
            self.reason = "OK"

        def stream(self, chunk_size):
            # Two partial chunks that form "foo":"bar" plus a second object
            yield b'{"foo":"b'
            yield b'ar"}\n{"hello":"world"}'

        def release_conn(self):
            pass

    mock_response = FakeHTTPResponse()
    mock_pool_manager.request.return_value = mock_response

    results = list(client.stream("GET", "http://example.com"))

    assert results == [{"foo": "bar"}, {"hello": "world"}]
    mock_pool_manager.request.assert_called_once()
    mock_pool_manager.clear.assert_called_once()


def test_stream_exception_in_chunks():
    mock_config = MagicMock(
        spec=[
            "verify_ssl",
            "ssl_ca_cert",
            "cert_file",
            "key_file",
            "assert_hostname",
            "retries",
            "socket_options",
            "connection_pool_maxsize",
            "timeout_millisec",
            "proxy",
            "proxy_headers",
        ]
    )
    mock_config.ssl_ca_cert = None
    mock_config.cert_file = None
    mock_config.key_file = None
    mock_config.verify_ssl = True
    mock_config.connection_pool_maxsize = 4
    mock_config.timeout_millisec = 5000
    mock_config.proxy = None
    mock_config.proxy_headers = None

    client = RESTClientObject(configuration=mock_config)
    mock_pool_manager = MagicMock()
    client.pool_manager = mock_pool_manager

    class FakeHTTPResponse:
        def __init__(self):
            self.status = 200
            self.reason = "OK"

        def stream(self, chunk_size):
            # Raise an exception while streaming
            raise ValueError("Boom!")

        def release_conn(self):
            pass

    mock_response = FakeHTTPResponse()
    mock_pool_manager.request.return_value = mock_response

    results = list(client.stream("GET", "http://example.com"))
    # Exception is logged, we yield nothing
    assert results == []
    mock_pool_manager.request.assert_called_once()
    mock_pool_manager.clear.assert_called_once()
