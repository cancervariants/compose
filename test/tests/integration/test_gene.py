"""Simple tests to confirm setup."""

import requests


def test_server_alive():
    """Gene server should return 200."""
    response = requests.get("http://gene/gene")
    assert response.status_code == 200, test_server_alive.__doc__


def test_swagger_ui():
    """Gene server should return swagger UI 'FastAPI - Swagger UI'."""
    response = requests.get("http://gene/gene")
    assert response.status_code == 200, test_swagger_ui.__doc__
    assert 'FastAPI - Swagger UI' in response.text, test_swagger_ui.__doc__


def test_query():
    """Gene server should find `BRCA2`."""
    url = "http://gene/gene/search?q=BRCA2&keyed=true"
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, test_query.__doc__
