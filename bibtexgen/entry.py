from .utils import getCitation
from tqdm import tqdm
import requests

semantic_scholar_base_path = "https://api.semanticscholar.org/v1/paper/"


def main():
    print("\n\n================================= Welcome to BibTex Generator =================================\n\n")
    paper_id = input("Please enter the Sematic Scholar Id of your paper: ")
    response = requests.request(
        url=semantic_scholar_base_path + paper_id, method='GET')
    data = response.json()
    print("\nName of paper: %s" % data['title'])
    print("\nCreating file %s_references.bib" % paper_id)
    f = open("%s_references.bib\n" % paper_id, 'wb')
    for reference in tqdm(data['references'], unit='papers'):
        f.write(getCitation(reference["paperId"]).encode('utf-8'))
        f.write("\n\n".encode('utf-8'))
    f.close()
    print("\nYour references have been saved!")
