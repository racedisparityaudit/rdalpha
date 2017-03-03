
class Page(object):
    def __init__(self, uri:str, name:str):
        self.uri = uri
        self.name = name

class MeasurePage(Page):
    def __init__(self, uri:str, name:str, measure_name:str):
        super().__init__(uri=uri, name=name)
        self.measure_name = measure_name

        self.source = ""
        self.first_published = ""
        self.last_updated = ""

        self.introduction = ""
        self.summary = ""

        self.download = ""
