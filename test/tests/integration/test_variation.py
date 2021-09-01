"""Simple tests to confirm setup."""

import requests


def test_server_alive():
    """Variation server should return 200."""
    response = requests.get("http://variation/variation")
    assert response.status_code == 200, test_server_alive.__doc__


def test_swagger_ui():
    """Variation server should return swagger UI 'FastAPI - Swagger UI'."""
    response = requests.get("http://variation/variation")
    assert response.status_code == 200, test_swagger_ui.__doc__
    assert 'FastAPI - Swagger UI' in response.text, test_swagger_ui.__doc__


def test_query():
    """Variation server should find `BRAF V600E`."""
    url = "http://variation/variation/normalize?q=BRAF%20V600E"
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, test_query.__doc__
