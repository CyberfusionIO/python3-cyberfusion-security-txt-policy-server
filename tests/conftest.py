import pytest
from starlette.testclient import TestClient

from cyberfusion.SecurityTXTPolicyServer import app


@pytest.fixture
def test_client() -> TestClient:
    return TestClient(app)
