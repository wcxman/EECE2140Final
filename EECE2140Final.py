import numpy as np
import matplotlib as mp
import csv
import scipy
import math

class dataset:
    def __init__(self, filename, frequency):
        with open(str(filename), mode = 'r') as file: #Opens the CSV file in a read mode
            self.csvfile = csv.reader(file) #Sets this object's data set to the contents of the CSV file
        self.frq = frequency
    def curvefit():
        return 0 #to implement
    def stdv(thelist):
        sum = 0 #Sum of the list
        for i in thelist:
            sum += i #Adds the value of each index to the sum
        avg = sum/len(thelist) #Average is sum divided by number of entries
        numerator = 0 #Numerator for standard deviation
        for i in thelist: #For each value in the list
            numerator += (i - avg)**2 #Adds the difference between the value at the array and the average, all squared
        return math.sqrt(numerator/(len(thelist)-1)) #Returns the formula for standard deviation
        