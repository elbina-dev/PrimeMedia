import os
import sys

import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app as flask_app

KNOWN_SECTIONS = ["/", "/about", "/movies", "/songs", "/books", "/courses", "/contact"]


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as test_client:
        yield test_client


def registered_routes():
    live_rules = {rule.rule for rule in flask_app.url_map.iter_rules()}
    return sorted(section for section in KNOWN_SECTIONS if section in live_rules)


def test_home_route_exists_and_works(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.parametrize("route", registered_routes())
def test_implemented_route_returns_200(client, route):
    response = client.get(route)
    assert response.status_code == 200, f"{route} is registered but broken"


@pytest.mark.parametrize("route", registered_routes())
def test_implemented_route_never_server_errors(client, route):
    response = client.get(route)
    assert response.status_code < 500, f"{route} threw a server error"