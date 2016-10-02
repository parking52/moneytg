__author__ = 'melchior'

import numpy as np
from bokeh.plotting import figure, show, output_file

n = 100000  # iterations
m = 30  # n_spells

def function(n_spells, iterations, size_sample, file_name):

    array_n_spells = np.zeros(n_spells)

    for n_spells in range(n_spells):

        deck = np.zeros(99)
        deck[:n_spells] = 1
        np.random.shuffle(deck)
        result_array = np.zeros(size_sample+1)

        for i in range(iterations):
            np.random.shuffle(deck)
            value_in_sample = sum(deck[:size_sample])
            result_array[value_in_sample] += 1

        value_for_n = 1 - (result_array[0])/iterations
        array_n_spells[n_spells] = value_for_n

    print("proba d'avoir au moins une carte")
    print(array_n_spells)
    if file_name is None:
        return array_n_spells
    else:
        p = figure(title=file_name)
        p.line(range(len(array_n_spells)), array_n_spells, line_color="black")
        output_file(file_name, title=file_name)
        show(p)




print("running smtg")
#check narset n_spell
# function(n_spells=30, iterations=100000, size_sample=4, file_name='narset')
# [ 0.       0.04113  0.07989  0.12062  0.15422  0.18925  0.22481  0.25788
#   0.28892  0.32299  0.35324  0.3786   0.40905  0.43423  0.46036  0.48594
#   0.51063  0.53645  0.55616  0.5767   0.60017  0.61991  0.64283  0.65695
#   0.67684  0.69522  0.71117  0.72838  0.74237  0.75573]
# 15 to have >.5 to get one.


#check caillou dans main de depart
# function(n_spells=20, iterations=100000, size_sample=7, file_name='narset_cailloux')
# [ 0.       0.07096  0.13715  0.20056  0.25895  0.31162  0.36465  0.41333
#   0.46108  0.49415  0.53712  0.57313  0.60645  0.6393   0.66814  0.69597
#   0.72368  0.74262  0.76756  0.78721]
# 10 to have at least 1 caillou

#check sidisi pour proba 3
# function(n_spells=50, iterations=100000, size_sample=3, file_name='sidisi')
# [ 0.       0.02976  0.06087  0.0889   0.11829  0.14699  0.17238  0.20033
#   0.22677  0.25345  0.27461  0.29944  0.32477  0.34413  0.37147  0.39174
#   0.41442  0.43518  0.45533  0.47829  0.49256  0.51238  0.53593  0.55055
#   0.56819  0.58727  0.60473  0.6171   0.63556  0.6483   0.66476  0.67967
#   0.69582  0.70595  0.72241  0.73544  0.74849  0.75905  0.76995  0.78157
#   0.79542  0.8042   0.81375  0.82481  0.83297  0.8421   0.8502   0.85942
#   0.86461  0.87559]
#  looks like 21
#  current status: 40 => 79%
#  fatass: 10 =>25%

