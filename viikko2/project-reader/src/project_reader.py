from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        data = toml.loads(content)
        
        project_name = data.get('tool', {}).get('poetry', {}).get('name', 'Unknown')
        project_description = data.get('tool', {}).get('poetry', {}).get('description', 'No description')
        project_license = data.get('tool', {}).get('poetry', {}).get('license', 'No license')
        project_authors = data.get('tool', {}).get('poetry', {}).get('authors', []) 
        dependencies_data = data.get('tool', {}).get('poetry', {}).get('dependencies', {})
        dev_dependencies_data = data.get('tool', {}).get('poetry', {}).get('dev-dependencies', {})

        project = Project(name=project_name, description=project_description, license=project_license, authors=project_authors, dependencies=dependencies_data, dev_dependencies=dev_dependencies_data) 
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return project

