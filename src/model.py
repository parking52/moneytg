import pandas as pd
from sklearn import linear_model
import pickle

df = pd.read_pickle('../data/Allsets_as_pd_cleaned.pck')
map = pickle.load(open("../data/mapping.pck", "rb"))
map_inverse = pickle.load(open("../data/mapping_inverse.pck", "rb"))

list_of_features = [
    'colors',
    'supertypes',
    'types',
    'power',
    'toughness',
    'loyalty',
    'rarity',
    # 'set',
    # 'reserved',
]

list_of_target = [
    'cmc'
]

df = df[list_of_target + list_of_features].astype('float')
clf = linear_model.LinearRegression()
clf.fit(df[list_of_features], df[list_of_target])

print(clf.coef_)

# predict ['colors', 'supertypes', 'types', 'power', 'toughness', 'loyalty', 'rarity', 'set', 'reserved']
# 	Anafenza, Kin-Tree
# clf.predict([1, 1, 0, 2, 2, 0, 0, 130, 0])
clf.predict([1, 1, 0, 2, 2, 0, 0])
#   Avacyn 8
# clf.predict([1, 1, 0, 8, 8, 0, 1, 55, 0])
clf.predict([1, 1, 0, 8, 8, 0, 1])

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
model = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
model.fit(df[list_of_features], df[list_of_target])
score = model.score(df[list_of_features], df[list_of_target])

# 	Anafenza, Kin-Tree
# model.predict([1, 1, 0, 2, 2, 0, 0, 130, 0])
model.predict([1, 1, 0, 2, 2, 0, 0])
#   Avacyn 8
# model.predict([1, 1, 0, 8, 8, 0, 1, 55, 0])
model.predict([1, 1, 0, 8, 8, 0, 1])

model = AdaBoostClassifier()
model.fit(df[list_of_features], df[list_of_target])
score = model.score(df[list_of_features], df[list_of_target])

# 	Anafenza, Kin-Tree
# model.predict([1, 1, 0, 2, 2, 0, 0, 130, 0])
model.predict([1, 1, 0, 2, 2, 0, 0])
#   Avacyn 8
# model.predict([1, 1, 0, 8, 8, 0, 1, 55, 0])
model.predict([1, 1, 0, 8, 8, 0, 1])

pass