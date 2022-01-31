import requests

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        return requests.get(self._url).json()
        