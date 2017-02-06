import sys
from pynt import task
sys.path.insert(0, '')

from taskrunners.CsvStructureBuilder import CsvStructureBuilder

@task()
def build_input_taxonomy_from_csv():
    '''Build the input taxonomy from scratch using the csv spreadsheet.'''
    print('Building input taxonomy')
    builder = CsvStructureBuilder("data/input/taxonomy.csv", "data/output/taxonomy.csv")
    builder.build()



__DEFAULT__=build_input_taxonomy_from_csv

if __name__ == "__main__":
    build_input_taxonomy_from_csv()