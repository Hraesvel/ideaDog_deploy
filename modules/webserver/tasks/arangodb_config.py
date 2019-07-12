#!/usr/bin/env python3
# added the relationship graph to a arangoDB DB
from sys import exit
import base64
import requests

class ArangoConfig():

    n_attr = 0
    base = None
    db_name = None
    password = None
    username = None

    def __init__(self, **kawrs):
        for k,v in kawrs.items():
            self.n_attr += 1
            setattr(self, k, v)

        self.base = base64.b64encode(str.encode(f"{self.username}:{self.password}")).decode()
    
    def add_graph(self):
        if self.n_attr < 4:
            print(f"Usage: Database name, username, password")
            exit(-1)

        url = f"http://localhost:8529/_db/{self.db_name}/_api/gharial"

        payload = "{\n\t\"name\": \"rel\",\n\t\"edgeDefinitions\": [\n            {\n                \"collection\": \"bearer_to_user\",\n                \"from\": [\n                    \"bearer_tokens\"\n                ],\n                \"to\": [\n                    \"users\"\n                ]\n            },\n            {\n                \"collection\": \"idea_owner\",\n                \"from\": [\n                    \"ideas\"\n                ],\n                \"to\": [\n                    \"users\"\n                ]\n            },\n            {\n                \"collection\": \"idea_voter\",\n                \"from\": [\n                    \"ideas\"\n                ],\n                \"to\": [\n                    \"users\"\n                ]\n            },\n            {\n                \"collection\": \"tag_to_idea\",\n                \"from\": [\n                    \"tags\"\n                ],\n                \"to\": [\n                    \"ideas\"\n                ]\n            }\n        ]\n}"
        headers = {
            'Content-Type': "application/json",
            'Authorization': f"Basic {self.base}",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "localhost:8529",
            'accept-encoding': "gzip, deflate",
            'content-length': "926",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

    def add_user(self):
        pass