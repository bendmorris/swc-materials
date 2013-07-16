* Write a script to read in time_series_data.txt
    * file objects - they have methods (e.g. read, write)
    * other things have the same methods (e.g. sys.stdout)
* Basics: what is a class/object, define a simple class, members, methods, 
    constructors 
* "Time Series" class: takes a list of data points [(x,y)], has a "get"
    method to get value at point x (convert list into dictionary); this class
    is an interface
* Inheritance: a Time Series class with step function interpolation 
* LinearTimeSeries: Linear interpolation
* QuadraticTimeSeries: quadratic interpolation (separate out "weighted average" 
    function from LinearTimeSeries)
* viewer.py: load in data file time_series_data.txt, implement a "view" method
    in the parent TimeSeries class that draws a scatter plot of a fine mesh
    around the data points