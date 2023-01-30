import requests
import time
from tqdm import tqdm


class Yandex:

    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def create_folder(self, folder_name):
        url = self.host + "v1/disk/resources"
        headers = self.get_headers()
        params = {"path": folder_name}
        response = requests.put(url=url, headers=headers, params=params)
        if response.status_code == 201:
            print("Folder is create!")
        elif response.status_code == 409:
            print('Folder with that name already exists!')
        else:
            print(response.status_code)

    def uploads(self, file_url, file_name):
        url = self.host + "v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": f'{file_name}', "url": file_url}
        response = requests.post(url=url, headers=headers, params=params)
        if response.status_code == 202:
            for _ in tqdm(range(100)):
                time.sleep(0.01)
            print("File is downloaded!")
        else:
            print(response.status_code)
