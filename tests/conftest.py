import pytest
from starlette.testclient import TestClient

from security_txt_policy_server import app


@pytest.fixture
def test_client() -> TestClient:
    return TestClient(app)
