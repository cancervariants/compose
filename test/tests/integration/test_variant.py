"""Simple tests to confirm setup."""

import requests


def test_server_alive():
    """Variant server should return 200."""
    response = requests.get("http://variant/variant")
    assert response.status_code == 200, test_server_alive.__doc__


def test_swagger_ui():
    """Variant server should return swagger UI 'FastAPI - Swagger UI'."""
    response = requests.get("http://variant/variant")
    assert response.status_code == 200, test_swagger_ui.__doc__
    assert 'FastAPI - Swagger UI' in response.text, test_swagger_ui.__doc__


def test_query():
    """Variant server should find `BRCA2`."""
    url = "http://variant/variant/normalize?q=BRAF%20V600E"
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, test_query.__doc__
