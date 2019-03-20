import multiprocessing
import urllib
from multiprocessing.pool import Pool

import urllib3
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from threading import Thread


def link_status(link):
    try:
        req = urllib.request.Request(url=link)
        resp = urllib.request.urlopen(req)

        if resp.status in [400, 404, 403, 408, 409, 501, 502, 503]:
            print(f"ERROR : ! Link is broken {resp.status} - {resp.reason} --> {link}")
        print(f"checking link.... {link} status : {resp.status}")
    except Exception as e:
        print(f"ERROR -->{e}")


req = Request("https://www.guardicore.com/")
page_content = urlopen(req)
# print(type(page_content))
#
soup = BeautifulSoup(page_content, features="html.parser")
# print(soup)

links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))


# print(len(links))

# print(link for link in links if "http" in link)
def run_fucker(links):
    for link in links:
        link_status(link)


pool = multiprocessing.Pool()
result = pool.map(run_fucker(links))
