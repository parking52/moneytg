__author__ = 'melchior'

import numpy as np
from quick_narset_values import function
from bokeh.plotting import figure, show, output_file

size_sample = 7
iterations = 100000
result_array = np.zeros((25, 8))
file_name='lands.html'

p = figure(title=file_name)

for n_lands in range(25, 50):

        deck = np.zeros(99)
        deck[:n_lands] = 1
        print("iter  " + str(n_lands))

        for i in range(iterations):
            final_idx = n_lands-25
            np.random.shuffle(deck)
            value_in_sample = sum(deck[:size_sample])
            result_array[final_idx][value_in_sample] += 1

        # p.line(range(len(result_array[final_idx])), result_array[final_idx] / iterations, line_color="black")


result_array = result_array / iterations
# final_indexes = np.matrix(np.repeat(range(size_sample+1), 25, axis=0)).tolist()[0]
final_indexes = np.array([np.array(range(size_sample+1)),]*25).tolist()
final_array = np.matrix(result_array).tolist()

color_dict = [list(range(0, 250, 10)), list(range(250, 0, -10))]
my_color_map = ["rgb({!s},{!s},{!s})".format(20, green_val, blue_val) for blue_val, green_val in zip(color_dict[0], color_dict[1])]
p.multi_line(
    xs=final_indexes,
    ys=final_array,
    line_color=my_color_map,
)

output_file(file_name, title=file_name)
show(p)