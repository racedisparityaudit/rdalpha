from model.Uri import Uri


class Page(object):
    def __init__(self, uri: Uri = Uri(), name: str = "", level: str = "", description: str = ""):
        self.uri = uri
        self.name = name
        self.level = level
        self.description = description

    def is_child_of(self, page):
        return page.uri.is_child_of(self.uri)

class Homepage(Page):
    subpages = []
    def __init__(self, tier_1_pages):
        super(Homepage, self).__init__(uri=Uri(),
                                       name="Homepage",
                                       level="T0",
                                       description="Racial Disparity Audit Homepage")
        self.subpages = []
        for node in tier_1_pages:
            self.subpages.append( {'uri': node.uri.full, 'name': node.name} )



class TierOnePage(Page):
    def __init__(self, uri, name, description, taxonomy, tier_2_pages):
        super(TierOnePage, self).__init__(uri=uri,
                                          name=name,
                                          level="T1",
                                          description=description)
        self.subpages = []
        for node in tier_2_pages:
            self.subpages.append( {'uri': node.uri, 'name': node.name} )


class TierTwoPage(Page):
    subpages = []
    def __init__(self, uri, name, description, taxonomy, tier_3_pages):
        super(TierTwoPage, self).__init__(uri=uri,
                                          name=name,
                                          level="T2",
                                          description=description,
                                          taxonomy=taxonomy)
        for node in tier_3_pages:
            self.subpages.append( {'uri': node.uri, 'name': node.name} )


class TierThreePage(Page):
    questions = []

    def __init__(self, uri, name, description, taxonomy, data_landing_pages):
        super(TierThreePage, self).__init__(uri=uri,
                                          name=name,
                                          level="T3",
                                          description=description,
                                          taxonomy=taxonomy)
        for node in data_landing_pages:
            self.questions.append({'uri': node.uri, 'name': node.name})


class DataLandingPage(Page):
    measures = []
    def __init__(self, uri, name, description, taxonomy, measures):
        super(DataLandingPage, self).__init__(uri=uri,
                                            name=name,
                                            level="T4",
                                            description=description,
                                            taxonomy=taxonomy)
        for node in measures:
            self.measures.append({'uri': node.uri, 'name': node.name})


class Measure(Page):
    def __init__(self, uri, name, description, taxonomy, slices = []):
        super(Measure, self).__init__(uri=uri,
                                            name=name,
                                            level="Measure",
                                            description=description,
                                            taxonomy=taxonomy)
        self.slices = slices



class Slice(Page):
    def __init__(self, uri, name, description, taxonomy):
        super(Slice, self).__init__(uri=uri,
                                      name=name,
                                      level="Slice",
                                      description=description,
                                      taxonomy=taxonomy)