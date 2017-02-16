import sys
from pynt import task
sys.path.insert(0, '')

from databuilder.taskrunners.taxonomy.CsvStructureBuilder import CsvStructureBuilder
from databuilder.taskrunners.data.DataImporter import XYMeasureListImporter
from databuilder.taskrunners.data.DataExporter import DataCSVExporter

@task()
def build_input_taxonomy_from_csv():
    '''Build the input taxonomy from scratch using the csv spreadsheet.'''
    print('Building input taxonomy')
    builder = CsvStructureBuilder("data/input/taxonomy.csv",
                                  "data/input/questions.csv",
                                  "data/output/taxonomy.csv")
    builder.build()

@task()
def convert_xy_file_to_cube():
    '''Build the input taxonomy from scratch using the csv spreadsheet.'''
    print('Importing data sheet')
    importer = XYMeasureListImporter()
    serieses = importer.import_spreadsheet("data/input/datasets/key_stage_2_2016.csv",
                                ['REGION_NAME', 'LA_NAME'],
                                ['Ethnicity'])

    print('Exporting to data/output/ks2')
    exporter = DataCSVExporter()
    exporter.export_to_table("data/output/datasets/key_stage_2_table.csv", serieses)

__DEFAULT__=build_input_taxonomy_from_csv

if __name__ == "__main__":
    convert_xy_file_to_cube()