import pandas as pd
from sklearn import linear_model


df = pd.read_pickle('../data/Allsets_as_pd_cleaned.pck')

list_of_features = [
    'colors',
    'supertypes',
    'types',
    'rarity',
    'set',
    'reserved'
]

list_of_target = [
    'cmc'
]

df = df[list_of_target + list_of_features].astype('float')
clf = linear_model.LinearRegression()
clf.fit(df[list_of_features], df[list_of_target])

print(clf.coef_)


pass