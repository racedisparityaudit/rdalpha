import csv
from databuilder.model.Data import DataPoint, DataSeries

class MeasureImporter(object):

    def import_series(self, file, category_columns, value_column) -> DataSeries:

        series = DataSeries(category_columns=category_columns, value_column=value_column)
        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)

            header_row = csv_reader.__next__()
            value_index = self.find_column(header_row, value_column)
            category_indexes = self.find_category_indexes(header_row, category_columns)

            for row in csv_reader:
                value = row[value_index]
                categories = [row[index] for index in category_indexes]
                point = DataPoint(value, categories)
                series.points.append(point)

        return series

    def find_category_indexes(self, header_row, category_columns):
        return [self.find_column(header_row, column) for column in category_columns]

    def find_column(self, header_row, column_header):
        return header_row.index(column_header)