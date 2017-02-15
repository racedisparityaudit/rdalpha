
class DataPoint(object):
    def __init__(self, value, categories):
        self.value = value
        self.categories = categories

class DataSeries(object):

    def __init__(self, value_column, category_columns):
        self.value_column = value_column
        self.category_columns = category_columns
        self.points = []