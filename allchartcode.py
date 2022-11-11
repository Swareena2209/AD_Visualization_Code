# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 22:04:45 2022

@author: sware
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import pandas and matplotlib modules
import pandas as pd
import matplotlib.pyplot as plt

#read the data from csv file data1 into data, which will be used to plot line and bar chart
data = pd.read_csv("data1.csv")

#print the data as output 
print("Dataset for linegraph and barchart\n")
print(data)


#define a function named linegraph for representing the data in the form of a line graph
def linegraph():
    #call the function plot to display line graph and assign values to the arguments ie value in the X axis, Y axis and label for displaying the labels
    plt.plot(data["Year"], data["Brazil"], label="Brazil")  
    plt.plot(data["Year"], data["France"], label="France")
    plt.plot(data["Year"], data["Australia"], label="Australia")
    plt.plot(data["Year"], data["Argentina"], label="Argentina")
    plt.xlabel("Year") #call the xlabel function to assign the label name on X axis ie Year
    plt.ylabel("Population") #call the ylabel function to assign the label name on Y axis ie Population
    plt.title("HIV Prevalance") #call the title function to assign a title name to the chart
    plt.legend()
    plt.show() #call the show function to display the bar chart

#define a function barchart for representing the data in multiple barchart format for comparison
def barchart():
    #call the function bar and assign the required values to the arguments ie value for the X axis, Y axis, the thickness of each bar is set to 1.5, the width and color of each bar
    plt.bar(data["Year"]+0.00, data["Brazil"], label="Brazil", width = 1.5, color ='blue')
    plt.bar(data["Year"]+1.5, data["Argentina"], label="Argentina", width = 1.5, color ='green')
    plt.bar(data["Year"]+3.0, data["France"], label="France", width = 1.5, color ='red' )
    plt.bar(data["Year"]+4.5, data["Australia"], label="Australia", width = 1.5, color ='orange')
    
    plt.xlabel("Year") #call the xlabel function to assign the label name on X axis ie Year
    plt.ylabel("Population") #call the ylabel function to assign the label name on Y axis ie Population
    plt.title("HIV Prevalance") #call the title function to assign a title name to the chart
    plt.legend() # call the legend fucntion to display the label of each bar ie country name in this case
    plt.show() #call the show function to display the bar chart

#define a function named piechart for representing the data in the form of a piechart
def piechart():
    read_data = pd.read_csv("Piechartdataset.csv")#read the data of piechart from the csv file into read_data using the function read_csv 
    print("\n Data for piechart\n")
    print(read_data) #print the data as output for comparing the piechart and csv file data
    plt.pie(read_data["Value"],autopct= '%1.1f%%',startangle=120) #call the pie function to plot the data and assign the value to each argument needed,autopct for labelling the wedges and startangle to rotate the start value of the piechart  
    plt.title(" HIV Prevalance of 1990") #call the title function to assign a title name to the chart
    plt.legend(bbox_to_anchor = (1,1),labels=read_data["Country"]) #call legend function to represent the labels in the chart, in this case Country name has been selected as the label for each wedge 
    plt.show() #call the show function to display the chart

    
linegraph()# call the defined function linegraph to display the plot
barchart()#call the defined function barchart for displaying the chart
piechart()# call the defined function to display the data



