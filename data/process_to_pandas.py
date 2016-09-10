__author__ = 'melchior'

import json
import os
from pprint import pprint
import pandas as pd

class DataObject():

    def __init__(self):

        with open('AllSets.json') as data_file:
            self.object = json.load(data_file)

data = DataObject()


list_of_test_sets = []
for set in data.object:
    list_of_test_sets.append(pd.DataFrame(data.object[set]['cards']))


df_all_sets = pd.concat(list_of_test_sets)
df_all_sets.to_pickle('Allsets_as_pd.pck')


df_all_sets_read = pd.read_pickle('Allsets_as_pd.pck')
assert isinstance(df_all_sets_read, pd.DataFrame)
assert df_all_sets_read.size > 0

pass