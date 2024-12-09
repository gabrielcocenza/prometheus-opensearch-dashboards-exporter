# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.
"""Fixtures for unit tests"""

from unittest.mock import patch

import pytest

from src.collector import Config


@pytest.fixture
def mock_gauge():
    with patch("src.collector.GaugeMetricFamily") as mock:
        mock.return_value = mock
        yield mock


@pytest.fixture
def mock_config():
    mocked_config = Config("localhost", "my-user", "my-password")
    yield mocked_config


@pytest.fixture
def mock_collect_api_status(api_response):
    with patch("src.collector.collect_api_status") as mock:
        mock.return_value = api_response
        yield mock
