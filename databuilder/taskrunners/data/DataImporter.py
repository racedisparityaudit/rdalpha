import csv
import pandas as pd

from databuilder.model.Data import DataPoint, DataSeries
from typing import List

class SimpleMeasureImporter(object):

    def import_series(self, file, category_columns, value_column) -> DataSeries:

        series = DataSeries(category_columns=category_columns, measure=value_column)
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

class XYMeasureListImporter(object):

    """
    Import spreadsheets that take the following form

        X X X X
        Y Y Y Y
    X X . . . .
    X X . . . .
    X X . . . .

    Where X is a category for the data point and Y is the name of a measure
    """
    def import_spreadsheet(self, file, category_column_headers, category_row_names) -> List[DataSeries]:

        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)

            # store the values
            x_categories = [next(csv_reader) for category in category_row_names]

            # store the row which refers to each column's measure
            measure_row = next(csv_reader)

            headers = next(csv_reader)

            # find the indices for categories that come in columns
            y_category_indices = [headers.index(column) for column in category_column_headers]

            sheet = dict()
            for row in csv_reader:
                for col in range(0, len(row)):
                    measure = measure_row[col]
                    if measure != "":
                        datapoint = self.datapoint_for_cell(row, col, x_categories, y_category_indices)
                        try:
                            sheet[measure].points.append(datapoint);
                        except:
                            series = DataSeries(measure, category_column_headers + category_row_names)
                            series.points.append(datapoint)
                            sheet[measure] = series

        return [series for series in sheet.values()]

    def find_category_indexes(self, header_row, category_columns):
        return [self.find_column(header_row, column) for column in category_columns]

    def datapoint_for_cell(self, row, col, x_category_values, y_category_indices) -> DataPoint:
        value = row[col]
        categories = [row[ind] for ind in y_category_indices] + [x_category_row[col] for x_category_row in x_category_values]
        return DataPoint(value, categories)

class ExcelDataMeasuresImporter(object):

    def import_excel(self, file):
        pd.read_excel
        data = pd.read_excel(io=file, sheetname="Data")
        measures = pd.read_excel(io=file, sheetname="Measures")

        pd.groupby(measures,)