import pandas as pd
import numpy as np


class ProcessedData():

    def __init__(self):

        self.df = None


df_all = pd.read_pickle('Allsets_as_pd.pck')


columns = [
    'cmc',
    'manaCost',
    'colors',
    'supertypes',
    'types',
    'subtypes',
    'rarity',
    'text',
    'power',
    'toughness',
    'loyalty',
    'set',
    #'releaseDate',
    'reserved',
    'name'
]

inst = ProcessedData()
df = df_all[columns]

map_list_for_processing = {}
map_list_for_processing_inverse = {}


def process_cmc():

    def fill_cmc(row):
        return 0

    df.cmc = df.apply(lambda r: fill_cmc(r) if np.isnan(r['cmc']) else r['cmc'], axis=1)


def process_manaCost():

    df.manaCost = df.manaCost.str.replace('}{', '-')
    df.manaCost = df.manaCost.str.strip('{')
    df.manaCost = df.manaCost.str.strip('}')

    df.manaCost.fillna(0, inplace=True)
    general_replacement_of_enum('manaCost')

    pass


def process_colors():
    df['colors'] = df['colors'].str.join('-')
    general_replacement_of_enum('colors')
    pass

def process_supertypes():
    df['supertypes'] = df['supertypes'].str.join('-')
    df.supertypes = df.apply(lambda r: True if (str(r['supertypes']) == 'Legendary' or str(r['supertypes']) == 'Legendary-Snow') else False, axis=1)


def process_types():
    df['types'] = df['types'].str.join('-')
    general_replacement_of_enum('types')


def process_subtypes():
    df.drop(['subtypes'], 1, inplace=True)


def process_rarity():
    general_replacement_of_enum('rarity')


def process_text():
    pass


def process_power(df):
    median_power = 0
    df.power.fillna(median_power, inplace=True)

    df = df[df['power'] != '*']
    df = df[df['power'] != '1+*']
    df = df[df['power'] != '2+*']



def process_toughness(df):
    median_toughness = 0
    df.power.fillna(median_toughness, inplace=True)

    df = df[df['toughness'] != '*']
    df = df[df['toughness'] != '1+*']
    df = df[df['toughness'] != '2+*']
    df = df[df['toughness'] != '7-*']


def process_loyalty():
    median_loyalty = 0
    df.power.fillna(median_loyalty, inplace=True)


def process_set():

    general_replacement_of_enum('set')


def process_releaseDate():

    def fill_releaseDate(row):
        return '1999'

    df.releaseDate = df.apply(lambda r: fill_releaseDate(r) if str(r['releaseDate']) == 'nan' else r['releaseDate'].split('-')[0], axis=1)


def process_reserved():

    df['reserved'].fillna(False, inplace=True)


def general_replacement_of_enum(name_of_column):

    pd_mapping = pd.Series(df[name_of_column].unique()).to_dict()
    pd_mapping_inverse = {v: k for k, v in pd_mapping.items()}
    map_list_for_processing[name_of_column] = pd_mapping
    map_list_for_processing_inverse[name_of_column] = pd_mapping_inverse

    df[name_of_column] = df[name_of_column].replace(pd_mapping_inverse)
    pass


process_cmc()  # If cmc is nan is mainly because of lands => 0 as well
process_manaCost()  #
process_colors()  #
process_supertypes()  # Basically Legendary or not
process_types()  # Done too => mapping
process_subtypes()  # Too detailed imo, not to be removed
process_rarity()  #
process_text()  #
process_power(df)  #
process_toughness(df)  #
process_loyalty()  #
process_set()  #
process_reserved()  # Reserved Nan => False

# process_releaseDate()  # Too much NaN to understand

df.to_pickle('Allsets_as_pd_cleaned.pck')

pass