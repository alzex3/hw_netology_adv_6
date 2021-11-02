import requests
import pytest
from main import ya_tkn
from ya_path_class import YaPathCreator


@pytest.fixture()
def app():
    app = YaPathCreator(ya_tkn)
    return app


class Test:

    def test_path_created(self, app):
        assert app.path_create()[0].status_code == 201

        path_name = app.path_create()[1].replace(' ', '%20')
        path_url = f'https://cloud-api.yandex.net/v1/disk/resources?path={path_name}'
        result = requests.get(path_url, headers={'Authorization': app.token})

        assert result.status_code == 200
