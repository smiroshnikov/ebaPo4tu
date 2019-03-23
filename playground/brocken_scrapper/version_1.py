import multiprocessing
import urllib
from multiprocessing.pool import Pool

import urllib3
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from threading import Thread


def check_link_status(link):
    bad_links = []
    try:
        req = urllib.request.Request(url=link)
        resp = urllib.request.urlopen(req, timeout=4)

        if resp.status in [400, 404, 403, 408, 409, 501, 502, 503]:
            print(f"ERROR : ! Link is broken {resp.status} - {resp.reason} --> {link}")
            bad_links.append(link)

        print(f"checking link.... {link} status : {resp.status}")
    except Exception as e:
        print(f"ERROR -->{e}")
    finally:
        return bad_links


def create_href_list():
    request = Request("https://www.guardicore.com/")
    page_content = urlopen(request)
    soup = BeautifulSoup(page_content, features="html.parser")
    links = []

    for link_tag in soup.find_all('a'):
        clean_url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', str(link_tag))
        if type(clean_url) is list:
            for entry in clean_url:
                print(f"link found {entry}!")
                links.append(entry)
        else:
            print(f"link found {clean_url}!")
            links.append(clean_url)

    return links


def run_checker(links):
    for link in links:
        check_link_status(link)


# run_checker(links)

if __name__ == '__main__':
    import timeit

    l = create_href_list()
    print(len(l))
    print(type(l[0]))

    # full_link_list = create_href_list()
    # print(len(full_link_list))
    # print(timeit.timeit("test()", setup="from __main__ import test"))
    # print(timeit.timeit("create_href_list()", setup="from __main__ import create_href_list"))
