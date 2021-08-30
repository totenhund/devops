import pytest
from python_app.app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def client_test(app):
    return app.test_client()
