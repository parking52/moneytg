__author__ = 'melchior'


from bokeh.plotting import figure, show, output_notebook
import pandas as pd
import io

TESTDATA=io.StringIO("""1,3,123
1,4,97
1,5,83
1,6,192
2,3,126
2,3.5,97
2,4.6,102
2,5.8,45
""")

data_headers = ['eastings', 'northings', 'obs']
data_points = pd.read_csv(TESTDATA, header=None, names=data_headers)

my_color_map = ["rgb({!s},{!s},{!s})".format(20, green_val, blue_val) for blue_val, green_val in zip(data_points.obs, 255-data_points.obs)]

p=figure(x_range=(0, 5), y_range=(0, 10))
p.scatter(x=data_points.eastings, y=data_points.northings, size=25, fill_color=my_color_map)
show(p)