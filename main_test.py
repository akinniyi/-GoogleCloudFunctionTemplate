from flask import Flask, request
import pytest
from main import main

# Create a fake "app" for generating test request contexts.
@pytest.fixture(scope="module")
def app():
    return Flask(__name__)

def test_request(app):
    with app.test_request_context(method='GET', data="<baz>foo</baz>"):
        res = main(request)
        assert res == 'Hello World!'