"""Simple tests to confirm setup."""

import requests


def test_server_alive():
    """Disease server should return 200."""
    response = requests.get("http://disease/disease")
    assert response.status_code == 200, test_server_alive.__doc__


def test_swagger_ui():
    """Disease server should return swagger UI 'FastAPI - Swagger UI'."""
    response = requests.get("http://disease/disease")
    assert response.status_code == 200, test_swagger_ui.__doc__
    assert 'FastAPI - Swagger UI' in response.text, test_swagger_ui.__doc__


def test_query():
    """Disease server should find `common cold`."""
    url = "http://disease/disease/normalize?q=common%20cold"
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, test_query.__doc__
