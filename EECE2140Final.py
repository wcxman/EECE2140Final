import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit 
import math

class dataset:
    def __init__(self, filename, frequency, name):
        with open(str(filename), mode = 'r') as file: #Opens the CSV file in a read mode
            self.csvfile = csv.reader(file) #Sets this object's data set to the contents of the CSV file
            self.data = [[],[],[]] #Creates a variable for data, holding time, input voltage, and output voltage
            count = 0
            for line in self.csvfile: #For each line in the file
                count += 1 #Notes the line of the file being read
                if count >= 12: #If the line is 12 or higher
                    self.data[0].append(float(line[0])) #Adds the time to the time slot of data
                    self.data[1].append(float(line[1])) #Adds the in voltage to that slot
                    self.data[2].append(float(line[2])) #Adds out voltage etc.
            self.ts = self.data[0] #Makes own list for each variable for ease of use
            self.vins = self.data[1]
            self.vouts = self.data[2]
        self.frq = frequency
        self.name = name
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
    def vdrops(self):
        tor = [] #The list to return
        for i in range(0,len(self.vins)): #For each data point in the file
            tor.append(self.vouts[i]-self.vins[i]) #Adds the voltage drop of this datapoint
        return tor #Returns the list
    def makehistogram(self):
        plt.hist(self.vouts,bins=np.linspace(-2,2,100)) #Creates a histogram of the voltage drops in the dataset
        plt.xlabel("Change in voltage (V)") #Labeling and titling the graph in following lines
        plt.ylabel("Frequency (Number)")
        plt.title("Frequency of voltage drops in " + self.name)
        plt.show()
    def histogramdata(self,startbound,endbound,detail,data): #Very inefficient way to sort data into bins, to be improved in a later version
        xdata = np.linspace(startbound,endbound,detail) #Every bin for the X value
        raw = [] #A storage of the quantities of values in each bin
        totalsum = 0 #The total sum of all data points looked at
        for i in range(0,len(xdata)): #For each x data
            count = 0 #Number of points that fit
            for j in data: #For each voltage out
                if i is not len(xdata)-1:
                    if j >= xdata[i] and j < xdata[i+1]: #If this value is within this bin
                        count+=1 #Adds one to both the total count and this bin's count
                        totalsum+=1
                else:
                    if j >= xdata[i] and j < xdata[i]+((endbound-startbound)/detail):
                        count+=1
                        totalsum+=1
            raw.append(count) #Sets this bin's total amount of points to the raw data list
        tor = [] #To return
        for i in raw:
            tor.append(i/totalsum) #Percent of points that appear in this bin
        return tor
def Gauss(x, A, B): #Function for the form of Gaussian distribution, x is x values and A and B are arrays returned by the curve fit function
    y = A*np.exp((-1*B*x**2)) #
    return y
def main():
    data = dataset("acq0001.csv",10,"10Hz Trial 2") #Imports every file from acq0001 to acq0100, can be modified for any range of files
    for i in range(2,10):
        file = "acq000" + str(i) + ".csv"
        data.adddata(file)
    for i in range(10,100):
        file = "acq00" + str(i) + ".csv"
        data.adddata(file)
    data.adddata("acq0100.csv")
    plt.hist(data.vins,bins=np.linspace(-2,2,100))
    plt.xlabel("Voltage (V)")
    plt.ylabel("Frequency (Number)")
    plt.title("Input voltages of " + data.name)
    plt.show()
    
    plt.hist(data.vouts,bins=np.linspace(-2,2,100))
    plt.xlabel("Voltage (V)")
    plt.ylabel("Frequency (Number)")
    plt.title("Output voltages of " + data.name)
    plt.show()
    
    plt.hist(data.vdrops(),bins=np.linspace(-2,2,100))
    plt.xlabel("Voltage (V)")
    plt.ylabel("Frequency (Number)")
    plt.title("Change in voltages of " + data.name)
    plt.show()
    
    
    xdata = data.ts #The x data of the plot
    ydata = data.vins #The y data of the scatterplot
    xplot = np.linspace(min(xdata), max(xdata), 100) #Makes 100 x values within the bounds of xdata for a plot
    plt.scatter(xdata, ydata, s = 0.5) #Makes a scatterplot of x and y values
    plt.xlabel("Time (s)")
    plt.ylabel("Input voltage (V)")
    plt.title("Input Voltage vs. Time")
    plt.show()
    
    xdata = data.ts #The x data of the plot
    ydata = data.vouts #The y data of the scatterplot
    xplot = np.linspace(min(xdata), max(xdata), 100) #Makes 100 x values within the bounds of xdata for a plot
    plt.scatter(xdata, ydata, s = 0.5) #Makes a scatterplot of x and y values
    plt.xlabel("Time (s)")
    plt.ylabel("Output voltage (V)")
    plt.title("Output Voltage vs. Time")
    plt.show()
    
    xdata = data.ts #The x data of the plot
    ydata = data.vdrops() #The y data of the scatterplot
    xplot = np.linspace(min(xdata), max(xdata), 100) #Makes 100 x values within the bounds of xdata for a plot
    plt.scatter(xdata, ydata, s = 0.5) #Makes a scatterplot of x and y values
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage difference (V)")
    plt.title("Change in Voltage vs. Time")
    plt.show()
main()
