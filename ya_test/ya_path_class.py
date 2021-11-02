import requests
import time


class YaPathCreator:
    def __init__(self, token):
        self.token = token

    def path_create(self):
        path_name = time.strftime("%H-%M-%S %d-%m-%Y")
        path_put_url = f'https://cloud-api.yandex.net/v1/disk/resources?path={path_name}'
        result = requests.put(path_put_url, headers={'Authorization': self.token})
        return result, path_name
