import sys
from pynt import task
sys.path.insert(0, '')

from taskrunners.InputBuilder import InputBuilder

@task()
def build_input_taxonomy_from_csv():
    '''Build the input taxonomy from scratch using the csv spreadsheet.'''
    print('Building input taxonomy')
    builder = InputBuilder("data", "data/output/")
    builder.build()



__DEFAULT__=build_input_taxonomy_from_csv

if __name__ == "__main__":
    build_input_taxonomy_from_csv()