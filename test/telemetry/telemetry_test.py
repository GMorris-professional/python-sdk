"""
Python SDK for OpenFGA

API version: 1.x
Website: https://openfga.dev
Documentation: https://openfga.dev/docs
Support: https://openfga.dev/community
License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

from unittest.mock import patch

from openfga_sdk.telemetry.metrics import (
    TelemetryMetrics,
)


def test_metrics_lazy_initialization():
    with patch(
        "openfga_sdk.telemetry.telemetry.TelemetryMetrics"
    ) as mock_metrics_telemetry:
        from openfga_sdk.telemetry import Telemetry  # Import inside the patch context

        telemetry = Telemetry()

        # Ensure _metrics is initially None
        assert telemetry._metrics is None

        # Access the metrics property, which should trigger lazy initialization
        metrics = telemetry.metrics

        # Verify that a TelemetryMetrics object was created and returned
        assert metrics == mock_metrics_telemetry.return_value
        mock_metrics_telemetry.assert_called_once()

        # Access the metrics property again, no new instance should be created
        metrics_again = telemetry.metrics
        assert metrics_again == metrics
        mock_metrics_telemetry.assert_called_once()  # Should still be only called once


def test_metrics_initialization_without_patch():
    from openfga_sdk.telemetry import Telemetry  # Import the Telemetry class directly

    telemetry = Telemetry()

    # Access the metrics property, which should trigger lazy initialization
    metrics = telemetry.metrics

    # Verify that a real TelemetryMetrics object was created and returned
    assert isinstance(metrics, TelemetryMetrics)

    # Access the metrics property again, no new instance should be created
    metrics_again = telemetry.metrics
    assert metrics_again == metrics
