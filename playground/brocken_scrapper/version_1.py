import multiprocessing
import time
import urllib
from multiprocessing.pool import Pool

import urllib3
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from threading import Thread


def burning_hatred_for_regex(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)


def regex_link(url):
    """

    :param url: can be any string containing any number of URLs
    :return:  list of str representing url
    :return:  list of str representing url
    """
    # pattern = '(https?:[^>]*)\"'
    pattern = "(https?:[^>]*)\'"
    p = re.compile(pattern)
    url = p.findall(url)
    return url


def check_link_status(link):
    try:
        req = urllib.request.Request(url=link)
        resp = urllib.request.urlopen(req, timeout=4)
        print(f"checking link.... {link} status : {resp.status}")
        if resp.status in [400, 404, 403, 408, 409, 501, 502, 503]:
            print(f"ERROR : ! Link is broken {resp.status} - {resp.reason} --> {link}")
            return False

    except Exception as e:
        print(f"ERROR -->{e}")
        return False
    else:
        return True



def create_href_list():
    request = Request("https://www.guardicore.com/")
    page_content = urlopen(request)
    soup = BeautifulSoup(page_content, features="html.parser")
    links = []

    for ix, link_tag in enumerate(soup.find_all('a', href=True)):
        if "http" in link_tag['href']:
            # print(f"link is {link_tag['href']} count : {ix}")
            links.append(link_tag['href'])

    return links


def run_checker(links):
    for link in links:
        check_link_status(link)


# run_checker(links)

if __name__ == '__main__':
    start = time.time()

    link_list = create_href_list()
    end = time.time()
    print(f"tool {start - end}")
    for l in link_list:
        print(check_link_status(l))
    end = time.time()
    print(f"tool {start - end}")


