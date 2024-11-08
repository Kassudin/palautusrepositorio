from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        #tiedonston toml sisältö:
        parsed_toml = toml.loads(content)
        #print ("Sisältö:\n", parsed_toml)

        tool = parsed_toml.get("tool", {}).get("poetry", {})
        name = tool.get("name")
        description = tool.get("description")
        license = tool.get("license")
        authors = tool.get("authors", [])
        dependencies = tool.get("dependencies", {})
        dependencies_list = list(dependencies.keys())
        dev_dependencies = tool.get("group", {}).get("dev", {}).get("dependencies", {})
        dev_dependencies_list = list(dev_dependencies.keys())
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies_list, dev_dependencies_list)
        #python3 src/index.py