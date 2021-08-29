import base64
import json

import requests


def test_encode():

    data = {
        "mecthod" : "get",
        "url" : "http://127.0.0.1:9999/demo.txt",
        "heards": None
    }

    url = "http://127.0.0.1:9999/demo.txt"
    res = requests.get(url=url)
    r = json.loads(base64.b64decode(res.content))
    print(r)
