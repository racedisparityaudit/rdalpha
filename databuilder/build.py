#!/usr/bin/python

import sys
from pynt import task

@task()
def build_input_taxonomy_from_csv():
    '''Clean build directory.'''
    print('Building input taxonomy')

__DEFAULT__=build_input_taxonomy_from_csv