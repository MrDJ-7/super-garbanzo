import builder
import txtBuilder
import htmlBuilder
import catRequest


class Director:
    text = None

    def __init__(self, base_url, header, method):
        war1 = catRequest.CatRequest(base_url, header)
        self.text = war1.execute(method)

    def build(self):
        # builder.Builder.Write(self.text)
        txtBuilder.TxtBuilder.Write(self.text)
        htmlBuilder.HtmlBuilder.Write(self.text)


war_q = Director("https://catfact.ninja",
                 {'accept': 'application/json', 'X-CSRF-TOKEN': 'JbtMRoEKlMjqpLGppVDBmcnauRAhRnNHCSEOt0Pk'}, "/fact")
war_q.build()
