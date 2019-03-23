from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

my_code = """
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
"""

my_code = """
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
    """
