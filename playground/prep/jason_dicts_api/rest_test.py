from pprint import pprint

import requests

headers = {
    "Content-Type": "application/json",
    "SDUID": "5a5395a1df73ca0d8c5661fe"

}

if __name__ == '__main__':
    r = requests.get("https://10.20.4.30/api/sc/dashboard")
    # r = requests.get("https://10.20.4.30/api/sc/dashboard", headers=headers)
    pprint(r.json())
    print(r.content)
