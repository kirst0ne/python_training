import pytest
from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request, app):
    def fin():
        app.session.ensure_logout()
        app.destroy()
    request.addfinalizer(fin)
    return app
