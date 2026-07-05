"""Test configuration for Policy Analysis Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "policy-analysis-agent", "category": "Legal"}
