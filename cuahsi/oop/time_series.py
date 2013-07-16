class TimeSeries:
    '''Represents a time series of data with sparse and/or irregular sampling.

    Use TimeSeries.get(x) to get the value at time x.'''

    def __init__(self, data):
        if not data:
            raise Exception("Time series must have at least one data point.")
        self.data = {float(x):float(y) for (x, y) in data}

    def get(self, x):
        return self.data[x]

    def view(self, grain=0.01):
        import matplotlib.pyplot as plt
        import numpy as np

        xs = self.data.keys()
        xs = np.arange(min(xs), max(xs), grain)
        plt.scatter(xs, [self.get(x) for x in xs])
        plt.show()


class StepTimeSeries(TimeSeries):
    '''Implementation of Time Series with step function interpolation.'''

    def get(self, x):
        # find the closest x value to the requested x value
        closest_point = None
        for (xi, yi) in self.data.items():
            if closest_point is None:
                closest_point = (xi, yi)
            else:
                cx, cy = closest_point
                if abs(xi-x) < abs(cx-x):
                    closest_point = (xi, yi)
        return closest_point[1]


class InterpolatingTimeSeries(TimeSeries):
    '''Implementation of a Time Series with interpolation between data points.
    Default interpolation is linear.
    
    >>> data = InterpolatingTimeSeries([(1, 1), (2,3)])
    >>> round(data.get(1), 1)
    1.0
    >>> round(data.get(2), 1)
    3.0
    >>> round(data.get(1.5), 1)
    2.0
    '''

    def get(self, x):
        # find the two closest points on each side of the requested x value
        x_values = self.data.keys()
        x_values.sort()

        if x < x_values[0]:
            return self.data[x_values[0]]
        elif x > x_values[-1]:
            return self.data[x_values[-1]]
        elif x in self.data:
            return self.data[x]

        for (n, x_value) in enumerate(x_values):
            if x_value > x:
                boundaries = n-1, n
                break

        boundary_x_values = [x_values[n] for n in boundaries]
        boundary_distance = sum([abs(x-xi) for xi in boundary_x_values])
        boundary_y_values = [self.data[xi] for xi in boundary_x_values]
        weights = [boundary_distance - abs(x-xi) for xi in boundary_x_values]
        return self.weighted_average(boundary_y_values, weights)

    def weighted_average(self, values, weights):
        return sum([float(y)*weight/sum(weights) for y, weight in zip(values, weights)])


LinearTimeSeries = InterpolatingTimeSeries


class QuadraticTimeSeries(InterpolatingTimeSeries):
    def __init__(self, data, exp=2):
        TimeSeries.__init__(self, data)
        self.exp = exp

    def weighted_average(self, values, weights):
        return InterpolatingTimeSeries.weighted_average(self, values, [w**self.exp for w in weights])


if __name__ == '__main__':
    import doctest
    result = doctest.testmod()
    print result