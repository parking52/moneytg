__author__ = 'melchior'

import numpy as np
from bokeh.plotting import figure, show, output_file

n = 10000  # iterations
m = 20  # n_spells

array_n_spells = np.zeros(m)

for n_spells in range(m):

    deck = np.zeros(99)
    deck[:n_spells] = 1
    np.random.shuffle(deck)
    result_array = np.zeros(5)

    for i in range(n):
        np.random.shuffle(deck)
        value_n_4 = sum(deck[0:4])
        result_array[value_n_4] += 1

    value_for_n = 1 - (result_array[0])/n
    array_n_spells[n_spells] = value_for_n

print("proba d'avoir au moins un spell sur les 4")
print(array_n_spells)

p = figure(title="Narset")
p.line(range(len(array_n_spells)), array_n_spells, line_color="black")
output_file("narset.html", title="narset")
show(p)
