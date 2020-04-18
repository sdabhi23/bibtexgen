import requests
from bs4 import BeautifulSoup

semantic_scholar_base_path = "https://api.semanticscholar.org/v1/paper/"


def getCitation(paper_id):
    ref = getSemanticScholar(paper_id)
    result = ''

    try:
        if ref['doi'] is not None:
            response = requests.request(url="http://api.crossref.org/works/" +
                                        ref['doi'] + "/transform/application/x-bibtex", method='GET')
            result = response.text
        elif ref['arxivId'] is not None:
            result = getCitationArxiv(ref['arxivId'])
        else:
            result = '@inproceedings{' + 'pi_' + '_'.join(
                ref['authors'][0]['name'].split(' ')) + '_%s' % ref['year'] + ',\n\ttitle = {' + ref['title'] + '},\n\tauthor = {' + " and ".join(
                [author['name'] for author in ref['authors']]) + '},\n\tbooktitle = {{' + ref['venue'] + '}},\n\tyear={' + str(ref['year']) + '},\n}'
    except KeyError as err:
        print(err)

    return result.strip()


def getSemanticScholar(paper_id):
    response = requests.request(
        url=semantic_scholar_base_path + paper_id, method='GET')
    data = response.json()
    if data['doi'] is not None:
        return {"doi": data['doi'], 'arxivId': None}
    elif data['arxivId'] is not None:
        return {"arxivId": data['arxivId'], 'doi': None}
    else:
        return data


def getCitationArxiv(arxivId):
    response = requests.request(
        url="https://arxiv2bibtex.org/?q=" + arxivId + "&format=bibtex", method='GET')
    soup = BeautifulSoup(response.text.encode('utf-8'), features="html.parser")
    return soup.find_all('textarea')[0].get_text()
