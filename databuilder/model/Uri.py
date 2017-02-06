class UriPart(object):
    """
    A section of a uri
    """
    def __init__(self, text=""):
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


class Uri(object):
    def __init__(self, tier_1="", tier_2="", tier_3="", tier_4="", measure="", slice=""):

        self.tier_1 = UriPart(tier_1)
        self.tier_2 = UriPart(tier_2)
        self.tier_3 = UriPart(tier_3)
        self.tier_4 = UriPart(tier_4)
        self.measure = UriPart(measure)
        self.slice = UriPart(slice)
        self.calculate_uri()


    def calculate_uri(self):
        self.full = "/"
        self.full = self.full + self.tier_1.uri_part if self.tier_1.text != '' else self.full
        self.full = self.full + '/' + self.tier_2.uri_part if self.tier_2.text != '' else self.full
        self.full = self.full + '/' + self.tier_3.uri_part if self.tier_3.text != '' else self.full
        self.full = self.full + '/' + self.tier_4.uri_part if self.tier_4.text != '' else self.full

    def append_uri_part(self, append_to_uri, uri_part):
        if uri_part:
            return append_to_uri + "/" + uri_part
        else:
            return append_to_uri

    def is_child_of(self, parent_uri):
        return self.full.startswith(parent_uri.full + "/")
