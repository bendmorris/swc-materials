import time_series
import sys

try:
    exp = float(sys.argv[1])
except:
    exp = 1

data = []
data_file = open('time_series_data.txt')
for line in data_file:
    x, y = line.split(',')
    x, y = float(x), float(y)
    data.append((x,y))

ts = time_series.QuadraticTimeSeries(data, exp=exp)
ts.view()