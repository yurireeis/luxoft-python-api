import requests
import json


class HttpClient:

    def __init__(self, default_header=None):
        self.default_header = default_header if default_header else {}


    def request(self, verb, url, payload=None, headers=None):
        payload = json.dumps(payload) if payload else {}
        headers = json.dumps(headers) if headers else self.default_header
        response = requests.request("GET", url, headers=headers, data=payload)
        return json.loads(response.text.encode('utf8'))
