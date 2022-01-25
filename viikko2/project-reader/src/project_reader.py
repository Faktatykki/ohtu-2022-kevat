from urllib import request
from project import Project

import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_data = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(toml_data['tool']['poetry']['name'], toml_data['tool']['poetry']['description'], toml_data['tool']['poetry']['dependencies'], toml_data['tool']['poetry']['dev-dependencies'])
