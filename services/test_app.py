from app import app # Flask instance of the API


DEFAULT_PATH = "/"
HOME_PATH = '/home'
BANNER_PATH = '/static/images/banner-bg.png'


def test_default_path():
    response = app.test_client().get(DEFAULT_PATH)
    assert response.status_code == 200
    assert response.text == 'Visit /home for home page'


def test_home_route():
    response = app.test_client().get(HOME_PATH)
    assert response.status_code == 200
    assert "Realestates" in response.text

def test_banner_route():
    response = app.test_client().get(BANNER_PATH)
    assert response.status_code == 200
