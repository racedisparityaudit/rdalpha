import unittest
from unittest import TestCase
from databuilder.taskrunners.data.MeasureImporter import MeasureImporter

class TestMeasureImporter(TestCase):

    def test_find_column(self):
        # Given
        header_row = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

        # When
        importer = MeasureImporter()
        delta_index = importer.find_column(header_row, 'delta')

        # Then
        self.assertEqual(delta_index, 3)

    def test_find_category_columns(self):
        # Given
        header_row = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

        # When
        importer = MeasureImporter()
        column_indices = importer.find_category_indexes(header_row, ['bravo', 'delta'])

        # Then
        self.assertEqual(column_indices[0], 1)
        self.assertEqual(column_indices[1], 3)

    def test_import_series(self):
        # Given
        file = "test_data/example_data.csv"
        categories = ["Region_name","LA_name"]
        value = 'WHITE_LADEN_16'

        # When
        importer = MeasureImporter()
        series = importer.import_series(file=file, category_columns=categories, value_column=value)

        # Then
        self.assertEqual(len(series.points), 164)

        point = series.points[12]
        self.assertEqual(point.value, '1810')
        self.assertEqual(point.categories[0], 'North East')
        self.assertEqual(point.categories[1], 'Gateshead')

if __name__ == '__main__':
    unittest.main()