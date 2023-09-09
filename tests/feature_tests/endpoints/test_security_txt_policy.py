import pytest
from starlette.testclient import TestClient

# Error handling


def test_security_txt_policy_domain_not_exists(
    test_client: TestClient,
) -> None:
    """Test response when the domain doesn't exist in the database."""
    response = test_client.get(
        "/.well-known/security.txt", headers={"Host": "domlimev.nl"}
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "No security.txt policy exists for this domain."
    }


def test_security_txt_policy_domain_invalid(test_client: TestClient) -> None:
    """Test response when the domain is invalid."""
    response = test_client.get(
        "/.well-known/security.txt", headers={"Host": "123"}
    )
    assert response.status_code == 200
    assert response.json() == {"detail": "It seems like I'm alive."}


def test_security_txt_policy_domain_empty(test_client: TestClient) -> None:
    """Test response when the domain is empty."""
    response = test_client.get(
        "/.well-known/security.txt", headers={"Host": ""}
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Specify security.txt policy to look for."
    }


def test_security_txt_policy_domain_x_powered_by_header(
    test_client: TestClient,
) -> None:
    """Test that response has X-Powered-By header, and its value."""
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "use-for-other-tests.com"},
    )
    assert response.headers["x-powered-by"] == "security-txt-policy-server"


# Edge cases


def test_security_txt_policy_domain_case_insensitive(
    test_client: TestClient,
) -> None:
    """Test that lowercase version of domain matches non-lowercase domain in database."""
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "uppercaseurl.com"},
    )
    assert response.status_code == 200


def test_security_txt_policy_domain_wildcard(
    test_client: TestClient,
) -> None:
    """Test that domain is matched to security.txt policy for wildcard domain."""
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "test.wildcard.com"},
    )
    assert response.status_code == 200


# security.txt policy


def test_security_txt_policy_url_contacts(test_client: TestClient) -> None:
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "use-for-other-tests.com"},
    )
    assert (
        "Contact: https://example.com/contact1.html"
        in response.text.splitlines()
    )
    assert (
        "Contact: https://example.com/contact2.html"
        in response.text.splitlines()
    )


def test_security_txt_policy_email_contacts(test_client: TestClient) -> None:
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "use-for-other-tests.com"},
    )
    assert "Contact: mailto:foo@example.com" in response.text.splitlines()
    assert "Contact: mailto:bar@example.com" in response.text.splitlines()


def test_security_txt_policy_expires(test_client: TestClient) -> None:
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "use-for-other-tests.com"},
    )
    assert "Expires: 2023-09-08T17:34:33.000Z" in response.text.splitlines()


def test_security_txt_policy_encryption_key_urls(
    test_client: TestClient,
) -> None:
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "use-for-other-tests.com"},
    )
    assert (
        "Encryption: https://example.com/contact1.pgp"
        in response.text.splitlines()
    )
    assert (
        "Encryption: https://example.com/contact2.pgp"
        in response.text.splitlines()
    )


def test_security_txt_policy_acknowledgments_urls(
    test_client: TestClient,
) -> None:
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "use-for-other-tests.com"},
    )
    assert (
        "Acknowledgments: https://example.com/thanks1.txt"
        in response.text.splitlines()
    )
    assert (
        "Acknowledgments: https://example.com/thanks2.txt"
        in response.text.splitlines()
    )


def test_security_txt_policy_policy_urls(test_client: TestClient) -> None:
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "use-for-other-tests.com"},
    )
    assert (
        "Policy: https://example.com/security1.html"
        in response.text.splitlines()
    )
    assert (
        "Policy: https://example.com/security2.html"
        in response.text.splitlines()
    )


def test_security_txt_policy_opening_urls(test_client: TestClient) -> None:
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "use-for-other-tests.com"},
    )
    assert (
        "Hiring: https://example.com/jobs1.html" in response.text.splitlines()
    )
    assert (
        "Hiring: https://example.com/jobs2.html" in response.text.splitlines()
    )


def test_security_txt_policy_preferred_languages_urls(
    test_client: TestClient,
) -> None:
    response = test_client.get(
        "/.well-known/security.txt",
        headers={"Host": "use-for-other-tests.com"},
    )
    assert "Preferred-Languages: en, nl" in response.text.splitlines()
