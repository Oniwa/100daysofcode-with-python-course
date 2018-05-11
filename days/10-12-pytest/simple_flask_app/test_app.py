import pytest

import app

@pytest.fixture
def app():
    app = app.create_app()
    app.debug = True
    return app.test_client()

def test():
    res = app.get("/")
    assert res.status_code == 200
