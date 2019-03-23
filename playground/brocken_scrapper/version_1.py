import urllib
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def check_link_status(link):
    """

    :param link: URL  string to be checked
    :return: boolean  reflecting link state
    """
    try:
        req = urllib.request.Request(url=link)
        resp = urllib.request.urlopen(req, timeout=4)
        print(f"checking link.... {link} status : {resp.status}")
        # if resp.status in [400, 404, 403, 408, 409, 501, 502, 503]:
        #     print(f"ERROR : ! Link is broken {resp.status} - {resp.reason} --> {link}")
        #     return False
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


def main():

    link_set = create_unique_links_set()
    pool = ThreadPool(processes=16)
    gl, bl = pool.apply(execute_checker, args=(link_set,))

    pool.close()
    pool.join()

    print(f"{len(gl)} <---unique good links ,unique bad links --->{len(bl)}")

    with open('bad_links.txt', 'w') as f:
        for l in bl:
            f.writelines(l + "\n")


if __name__ == '__main__':
    main()
"http://qaru.site/questions/37986/how-to-get-the-return-value-from-a-thread-in-python"
