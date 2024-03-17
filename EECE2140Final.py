import numpy as np
import matplotlib as mp
import csv

class dataset:
    def __init__(self, filename, frequency):
        with open(str(filename), mode = 'r') as file: #Opens the CSV file in a read mode
            self.csvfile = csv.reader(file) #Sets this object's data set to the contents of the CSV file
        self.frq = frequency
        
            
            
    