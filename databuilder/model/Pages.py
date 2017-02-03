
class TaxonomyPart(object):
    """
    A section of a uri
    """
    def __init__(self, text):
        self.uri_part = self.convert_to_uri(text)
        self.text = text

    """
    Converts a string to a safe uri (probably a better library function)
    """
    def convert_to_uri(self, string):
        return string.replace('.', '') \
            .replace(',', '') \
            .replace('&', 'and') \
            .replace(' ', '') \
            .lower()


class Taxonomy(object):
    def __init__(self, tier_1="", tier_2="", tier_3="", tier_4=""):
        self.tier_1 = TaxonomyPart(tier_1)
        self.tier_2 = TaxonomyPart(tier_2)
        self.tier_3 = TaxonomyPart(tier_3)
        self.tier_4 = TaxonomyPart(tier_4)
        self.calculate_uri()

    def calculate_uri(self):
        self.uri = self.tier_1.uri_part
        self.uri = self.uri + '/' + self.tier_2.uri_part if self.tier_2.text != '' else self.uri
        self.uri = self.uri + '/' + self.tier_3.uri_part if self.tier_3.text != '' else self.uri
        self.uri = self.uri + '/' + self.tier_4.uri_part if self.tier_4.text != '' else self.uri




class Page(object):
    def __init__(self, uri = "", name = "", level = "", description = "", taxonomy = Taxonomy()):
        self.uri = uri
        self.name = name
        self.level = level
        self.description = description
        self.taxonomy = taxonomy


class Homepage(Page):
    subpages = []
    def __init__(self, tier_1_pages):
        super(Homepage, self).__init__(uri="/",
                                          name="Homepage",
                                          level="T0",
                                          description="Racial Disparity Audit Homepage",
                                          taxonomy=Taxonomy())
        self.subpages = []
        for node in tier_1_pages:
            self.subpages.append( {'uri': node.uri, 'name': node.name} )



class TierOnePage(Page):
    def __init__(self, uri, name, description, taxonomy, tier_2_pages):
        super(TierOnePage, self).__init__(uri=uri,
                                          name=name,
                                          level="T1",
                                          description=description,
                                          taxonomy=taxonomy)
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