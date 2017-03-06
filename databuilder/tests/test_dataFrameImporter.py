import unittest
from unittest import TestCase
from databuilder.factories.DataFrameImporter import DataFrameImporter
import pandas as pd
import numpy as np


class TestDataFrameImporter(TestCase):

    def test_import_data_frame_with_ks4_example(self):
        data = DataFrameImporter().import_data_frame(excel_file='test_data/example_ks4.xlsx')
        self.assertIsNotNone(data)
        self.assertIsNot(0, len(data.index))

        expected_columns = ['Code', 'Measure', 'Time', 'Time_type', 'Race', 'Race_type',
                            'Location', 'Location_type', 'Income', 'Income_type',
                            'Gender', 'Age Bracket', 'Value']
        self.assertListEqual(list(data), expected_columns)

    def test_import_data_frame_with_unemployment_example(self):
        data_categories = ['Race', 'Race_type', 'Location', 'Location_type', 'Income', 'Income_type', 'Gender', 'Age Bracket']
        data = DataFrameImporter().import_data_frame(excel_file='test_data/example_unemployment.xlsx',
                                                     data_page_categories=data_categories)

        self.assertIsNotNone(data)
        self.assertIsNot(0, len(data.index))

        expected_columns = ['Code', 'Measure', 'Time', 'Time_type', 'Race', 'Race_type',
                            'Location', 'Location_type', 'Income', 'Income_type',
                            'Gender', 'Age Bracket', 'Value']
        self.assertListEqual(list(data), expected_columns)



if __name__ == '__main__':
    unittest.main()