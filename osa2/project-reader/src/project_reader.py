from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = tomllib.loads(content)
        project = data["project"]
        return Project(
            name=project["name"],
            description=project["description"],
            license=project["license"],
            authors=[author["name"] for author in project.get("authors", [])],
            dependencies=project["dependencies"],
            dev_dependencies=data["dependency-groups"]["dev"]
        )
