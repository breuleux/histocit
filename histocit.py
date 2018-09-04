
from urllib import parse
from bs4 import BeautifulSoup
import sys
import requests
import time


def readpage(url, query):
    req = requests.get(url, params=query)
    if 200 <= req.status_code < 300:
        return req.text
    else:
        raise Exception(f'Could not read page: Error {req.status_code}')


def citation_history(author):
    # First we need to find out what the author's Google Scholar uid is
    query = {'hl': 'en', 'q': author}

    html = readpage("https://scholar.google.ca/scholar", query)
    soup = BeautifulSoup(html, 'html.parser')
    href = soup.find(class_="gs_rt2").find('a')['href']
    uid = parse.parse_qs(parse.urlparse(href).query)['user'][0]

    # Now we can go to their citation page
    time.sleep(2)
    query = {'hl': 'en', 'user': uid}

    html = readpage("https://scholar.google.ca/citations", query)
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find(class_="gsc_md_hist_b")
    years = [child.string for child in data.find_all(class_="gsc_g_t")]
    cit = [child.string for child in data.find_all(class_="gsc_g_a")]

    return {y: c for y, c in zip(years, cit)}


if __name__ == '__main__':
    author = sys.argv[1]
    data = citation_history(author)
    print(f'Citation history for {author}')
    print('Year #Cit')
    for y, c in sorted(data.items()):
        print(f'{y} {c}')
