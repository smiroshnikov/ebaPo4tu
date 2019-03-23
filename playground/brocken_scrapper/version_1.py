import time
import urllib
import multiprocessing
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


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


def create_unique_links_set():
    """

    :return: collection of UNIQUE links located in page object
    """
    request = Request("https://www.guardicore.com/")
    page_content = urlopen(request)
    soup = BeautifulSoup(page_content, features="html.parser")
    links = set()

    for ix, link_tag in enumerate(soup.find_all('a', href=True)):
        if "http" in link_tag['href']:
            # print(f"link is {link_tag['href']} count : {ix}")
            links.add(link_tag['href'])

    return links


def create_links_list():
    """

    :return: collection of ALL links located in page object
    """
    request = Request("https://www.guardicore.com/")
    page_content = urlopen(request)
    soup = BeautifulSoup(page_content, features="html.parser")
    links = []

    for ix, link_tag in enumerate(soup.find_all('a', href=True)):
        if "http" in link_tag['href']:
            # print(f"link is {link_tag['href']} count : {ix}")
            links.append(link_tag['href'])

    return links


def execute_checker(links):
    good_links_set = set()
    bad_links_set = set()

    for link in links:
        if check_link_status(link):
            good_links_set.add(link)
        else:
            bad_links_set.add(link)
    return good_links_set, bad_links_set


if __name__ == '__main__':
    start = time.time()
    link_set = create_unique_links_set()
    gl, bl = execute_checker(link_set)

    print(f"{len(gl)} <---unique good links ,unique bad links --->{len(bl)}")
    end = time.time()
    print(f"tool {end - start}")
