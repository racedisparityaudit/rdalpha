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
    def __init__(self, tier_1="", tier_2="", tier_3="", tier_4="", measure="", slice=""):
        if tier_1 != "":
            self.tier_1 = TaxonomyPart(tier_1)
        if tier_2 != "":
            self.tier_2 = TaxonomyPart(tier_2)
        if tier_3 != "":
            self.tier_3 = TaxonomyPart(tier_3)
        if tier_4 != "":
            self.tier_4 = TaxonomyPart(tier_4)
        if measure != "":
            self.measure = TaxonomyPart(measure)
        if slice != "":
            self.slice = TaxonomyPart(slice)
        self.calculate_uri()

    def calculate_uri(self):
        self.uri = ""
        self.uri = self.tier_1.uri_part
        self.uri = self.uri + '/' + self.tier_2.uri_part if self.tier_2.text != '' else self.uri
        self.uri = self.uri + '/' + self.tier_3.uri_part if self.tier_3.text != '' else self.uri
        self.uri = self.uri + '/' + self.tier_4.uri_part if self.tier_4.text != '' else self.uri

    def append_uri_part(self, append_to_uri, uri_part):
        if uri_part:
            return append_to_uri + "/" + uri_part
        else:
            return append_to_uri
