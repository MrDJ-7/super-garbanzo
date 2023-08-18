import Request
import requests
import json


class CatRequest(Request.MyRequest):
    # MyRequestdef __init__(self,self base_url, header):
    #     super().__init__(base_url, header)
    #     self.method_name = None
    method_name = None

    def execute(self, method_name):
        self.method_name = method_name
        r = requests.get(self.base_url + self.method_name,
                         headers=self.header)
        # print(r.json())
        return r.json()
