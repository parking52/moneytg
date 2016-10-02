import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle
from sys import argv
from sklearn.externals import joblib

prompt = '> '
clf = joblib.load('../src/lin_model.pkl')

rarity_dict = {
    'Basic Land': 0,
    'Common': 1,
    'Uncommon': 2,
    'Special': 3,
    'Rare': 4,
    'Mythic Rare': 5
    }
dict_features_index = {
    'white': 0,
    'black': 1,
    'red': 2,
    'green': 3,
    'blue': 4,
    'supertypes': 5,
    'power': 6,
    'toughness': 7,
    'rarity': 8,
    'releaseDate': 9
}
n_features = len(dict_features_index)


def predict(dummy_input):
    values = dummy_input
    return clf.predict(values)

def ask_input():

    dict_input = np.zeros(n_features)

    print("I'd like to ask you a few questions.")
    print("Which color ? white black red green blue")
    color = input(prompt)
    dict_input[dict_features_index[color]] = 1

    print("Legendary ? 1/0")
    legendary = input(prompt)
    dict_input[dict_features_index['supertypes']] = 1

    print("Which power ?")
    power = input(prompt)
    dict_input[dict_features_index['power']] = power

    print("Which toughness")
    toughness = input(prompt)
    dict_input[dict_features_index['toughness']] = toughness

    print("Which rarity ? Basic Land    Common    Uncommon    Rare    Mythic Rare")
    rarity = input(prompt)
    dict_input[dict_features_index['rarity']] = rarity_dict[rarity]

    print("Which year of release ? ")
    releaseDate = input(prompt)
    dict_input[dict_features_index['releaseDate']] = releaseDate

    return dict_input

dummy_input = ask_input()
output = predict(dummy_input)
print(str(round(output[0][0])) + '       (' + str(output) + ')')
