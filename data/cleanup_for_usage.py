import pandas as pd
import numpy as np

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
df = df_all[columns]


def process_cmc():

    def fill_cmc(row):
        return 0

    df.cmc = df.apply(lambda r: fill_cmc(r) if np.isnan(r['cmc']) else r['cmc'], axis=1)


def process_manaCost():
    pass


def process_colors():
    pass


def process_supertypes():
    pass


def process_types():
    pass


def process_subtypes():
    pass


def process_rarity():
    pass


def process_text():
    pass


def process_power():
    pass


def process_toughness():
    pass


def process_loyalty():
    pass


def process_set():
    pass


def process_releaseDate():

    def fill_releaseDate(row):
        return '1999'

    df.releaseDate = df.apply(lambda r: fill_releaseDate(r) if str(r['releaseDate']) == 'nan' else r['releaseDate'].split('-')[0], axis=1)


def process_reserved():

    df.fillna(True, inplace=True)


process_cmc()  # If cmc is nan is mainly because of lands => 0 as well
process_manaCost()  #
process_colors()  #
process_supertypes()  #
process_types()  #
process_subtypes()  #
process_rarity()  #
process_text()  #
process_power()  #
process_toughness()  #
process_loyalty()  #
process_set()  #
# process_releaseDate()  # Too much NaN to understand
process_reserved()  # Reserved Nan => False

df.to_pickle('Allsets_as_pd_cleaned.pck')

pass