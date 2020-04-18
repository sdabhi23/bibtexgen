import requests
from .utils import getCitation


class bibtex():

    def __init__(self):
        self.base_path = "https://api.semanticscholar.org/v1/paper/"

    def generate_references(self, paper_id):

        response = requests.request(
            url=self.base_path + paper_id, method='GET')
        data = response.json()

        references = []
        for reference in data['references']:
            references.append(getCitation(
                reference["paperId"]).encode('utf-8'))

        return references
