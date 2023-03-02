import requests
from pprint import pprint
# import logging

# logging.basicConfig(level=logging.DEBUG)

TOKEN = 'YOUR_TOKEN'
file_path = 'test.txt'

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    
    def get_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "True"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload(self, file_path: str):
        link = self.get_link(file_path=file_path).get('href', '')
        with open(file_path, 'br') as file:
            response = requests.put(link, file)
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    uploader = YaUploader(TOKEN)
    result = uploader.upload(file_path)