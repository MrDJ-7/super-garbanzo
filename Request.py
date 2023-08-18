import requests
import json


class MyRequest:
    # base_url = ''
    # header = ''

    def __init__(self, base_url, header):
        self.base_url = base_url
        self.header = header


    def execute(self):
        pass



# war1 = MyRequest('https://catfact.ninja/fact',
#                  {'accept': 'application/json', 'X-CSRF-TOKEN': 'JbtMRoEKlMjqpLGppVDBmcnauRAhRnNHCSEOt0Pk'})
# war1.deserialize()
# war1.deserialize(r.json())
# print(f"Status Code: {r.status_code}, Content: {r.json()}")
# print(war1.deserialize())
# print(war1.r.json())