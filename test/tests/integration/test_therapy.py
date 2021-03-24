"""Simple tests to confirm setup."""

import requests


def test_server_alive():
    """Therapy server should return 200."""
    response = requests.get("http://therapy/therapy")
    assert response.status_code == 200, test_server_alive.__doc__


def test_swagger_ui():
    """Therapy server should return swagger UI 'FastAPI - Swagger UI'."""
    response = requests.get("http://therapy/therapy")
    assert response.status_code == 200, test_swagger_ui.__doc__
    assert 'FastAPI - Swagger UI' in response.text, test_swagger_ui.__doc__


def test_query():
    """Therapy server should find `cisplatin`."""
    url = "http://therapy/therapy/search?q=cisplatin&keyed=true"
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, test_query.__doc__