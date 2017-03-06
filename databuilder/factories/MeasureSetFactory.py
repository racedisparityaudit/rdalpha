import pandas as pd
from databuilder.model.Measure import MeasureSet
from databuilder.factories.DataFrameImporter import DataFrameImporter

class MeasureSetFactory(object):
    categories = []
    def __init__(self, categories = ['Race', 'Race_type', 'Location', 'Location_type', 'Income', 'Income_type', 'Time', 'Time_type']):
        self.categories = categories

    def build_measure_set(self, excel_file) -> MeasureSet:
        data = DataFrameImporter().import_data_frame(excel_file=excel_file)