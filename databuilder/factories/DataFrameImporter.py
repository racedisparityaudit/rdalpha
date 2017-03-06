import pandas as pd
import numpy as np

class DataFrameImporter(object):

    def import_data_frame(self, excel_file:str, data_page_categories = [], data_page = "Data", measures_page = "Measures") -> pd.DataFrame:
        """

        :param excel_file: path to an excel file
        :param data_page_category_columns: the category columns to be taken out of the data sheet
        :param data_page: the name of the data page in the excel workbook
        :param measures_page: the name of the measures page in the excel workbook
        :return: a pd dataframe of form [measure_code, measure_categories ..., data_categories ..., measure_value]
        """

        """ First we get the data """
        data = pd.read_excel(io=excel_file, sheetname=data_page).fillna('')
        measures = pd.read_excel(io=excel_file, sheetname=measures_page).fillna('')

        """ Build our template of the return dataset """
        categories = list(measures) + data_page_categories
        row_count = len(data.index)

        full_data = data
        for measure_column in list(measures):
            full_data[measure_column] = pd.Series(np.zeros(row_count))

        """ Main loop runs across the list of measures """
        results = pd.DataFrame(columns=categories + ['Value'])

        for index, measure_row in measures.iterrows():
            if measure_row['Code'] in full_data:

                """ Fill a copy of the table data with data for this measure from the measures sheet """
                tmp_data = full_data
                for measure_column in list(measures):
                    tmp_data[measure_column] = str(measure_row[measure_column])

                """ Get results we want """
                tmp_columns = categories + [measure_row['Code']]
                tmp_results = tmp_data[tmp_columns]

                """ Set to the appropriate column name """
                tmp_results.columns = categories + ['Value']
                results = results.append(tmp_results)
            else:
                print('Could not find data for column with code "' + str(measure_row['Code']) + '"')

        return results
