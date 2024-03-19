import numpy as np
import matplotlib as mp
import csv
import scipy
import math

class dataset:
    def __init__(self, filename, frequency):
        with open(str(filename), mode = 'r') as file: #Opens the CSV file in a read mode
            self.csvfile = csv.reader(file) #Sets this object's data set to the contents of the CSV file
            self.data = [[],[],[]] #Creates a variable for data, holding time, input voltage, and output voltage
            count = 0
            for line in self.csvfile: #For each line in the file
                count += 1
                if count >= 12: #If the line is 12 or higher
                    self.data[0].append(float(line[0])) #Adds the time to the time slot of data
                    self.data[1].append(float(line[1])) #Adds the in voltage to that slot
                    self.data[2].append(float(line[2])) #Adds out voltage etc.
            self.ts = self.data[0] #Makes own list for each variable for ease of use
            self.vins = self.data[1]
            self.vouts = self.data[2]
        self.frq = frequency
    def curvefit():
        return 0 #to implement
    def adddata(self,filename): #Method to add more data to the object's data with another CSV
        with open(str(filename),mode = 'r') as file: #Opens the CSV file in a read mode
            thisfile = csv.reader(file) #Creates a new file object for this file
            count = 0
            for line in thisfile:
                count += 1
                if count >= 12: #If the line is 12 or higher
                    self.data[0].append(float(line[0])) #Adds the time to the time slot of data
                    self.data[1].append(float(line[1])) #Adds the in voltage to that slot
                    self.data[2].append(float(line[2])) #Adds out voltage etc.
            self.ts = self.data[0] #Makes own list for each variable for ease of use
            self.vins = self.data[1]
            self.vouts = self.data[2]
    def stdv(thelist):
        sum = 0 #Sum of the list
        for i in thelist:
            sum += i #Adds the value of each index to the sum
        avg = sum/len(thelist) #Average is sum divided by number of entries
        numerator = 0 #Numerator for standard deviation
        for i in thelist: #For each value in the list
            numerator += (i - avg)**2 #Adds the difference between the value at the array and the average, all squared
        return math.sqrt(numerator/(len(thelist)-1)) #Returns the formula for standard deviation