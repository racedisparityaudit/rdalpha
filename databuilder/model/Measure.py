import pandas as pd

class DimensionList(object):
    def __init__(self, race_type = "ONS 2011 5", location_type = "National",
                 income_type = "Household Income", time_type = "Year", other = []):
        self.race_type = race_type
        self.location_type = location_type
        self.income_type = income_type
        self.time_type = time_type
        self.other = other

    def columns(self):
        return ['Race','Location','Income','Time'] + self.other

class Measure(object):

    def __init__(self, name:str, dimensions: DimensionList):
        self.name = name
        self.dimensions = dimensions
        self.values = pd.DataFrame(columns=self.dimensions.columns())

