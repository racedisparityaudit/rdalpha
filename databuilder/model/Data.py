
class DataPoint(object):
    def __init__(self, value, categories):
        self.value = value
        self.categories = categories

class DataSeries(object):

    def __init__(self, measure, category_columns):
        self.measure = measure
        self.category_columns = category_columns
        self.points = []

    def find(self, filter) -> DataPoint:
        match_values = list(filter.values())
        match_indices = [self.category_columns.index(key) for key in filter.keys()]
        for point in self.points:
            if self.check_point(point, match_indices, match_values):
                return point

    def check_point(self, point, match_indices, match_values):
        for i in range(0, len(match_indices)):
            point_value = point.categories[match_indices[i]]
            if point_value != match_values[i]:
                return False
        return True