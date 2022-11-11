# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:07:21 2022

@author: sahana muralidaran (21076516)
"""

import pandas as pd
import matplotlib.pyplot as plt

#function to plot 6 subplots showing the number of deaths for different regions 
def subplots():
    fig, axs = plt.subplots(2, 3, figsize=(18, 8))
    for i in range(n):
    #repeating for loop n times to cover all the regions
        plt.subplot(2,3,i+1)
        #create a new dataframe for all data of a single region
        group2= new_data.loc[(new_data['ParentLocation']== regions[i])]
        group1= group2.groupby(["Period"]).sum()
        years=[]
        for j in range(22):
        #repeating the loop 22 times to get the year values present in data
            year=group1.iloc[j].name
            years.append(year)
        plt.plot(years,group1['FactValueNumeric'],'.-',label=regions[i])
        plt.xlabel('Years')
        plt.ylabel('Number of HIV related deaths')
        plt.legend()
    plt.savefig("six_subplot.png")
    plt.show()


#function to create pie plot for the top 5 countries with highest number of HIV related deaths
def top5_piechart():
    total= new_data.drop(['Period'],axis=1)
    total = total.groupby(["Location"]).sum()
    new_total= total.sort_values(by='FactValueNumeric',ascending=False)
    top8= new_total.head(8)
    labels=[]
    for j in range(8):
    #repeating loop to get the country names inorder to create labels
        country=top8.iloc[j].name
        labels.append(country)
    plt.pie(top8['FactValueNumeric'],labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("Top 8 countries with the highest number of HIV related deaths\n"+
              "Year (2000 to 2021)")
    plt.savefig("pie_plot.png")
    plt.show()


#function to plot with multiple lines to show number of HIV related deaths in various regions
def multiline():
    for i in range(n):
        #create a new dataframe for all data of a single region
        group3= new_data.loc[(new_data['ParentLocation']== regions[i])]
        group4= group3.groupby(["Period"]).sum()
        years=[]
        for j in range(22):
        #loop to get the years from 2000 to 2021 for plotting the graph
            year=group4.iloc[j].name
            years.append(year)
        plt.plot(years,group4['FactValueNumeric'],label=regions[i])
    plt.xlabel('Years')
    plt.ylabel('Number of deaths')
    plt.title('Number of HIV related deaths for various regions')
    plt.legend()
    plt.savefig("multiline.png")
    plt.show()

#function to plot the bar graph to show the total number of HIV related deaths over the years
def bar_graph():
    plt.title('Number of HIV related deaths between 2000 and 2021')
    overall= new_data.groupby(["Period"]).sum()
    years=[]
    for j in range(22):
        #loop to get the years from 2000 to 2021 for plotting the graph
        year=overall.iloc[j].name
        years.append(year)
    plt.bar(years,overall['FactValueNumeric'],label='World')
    plt.xlabel('Years')
    plt.ylabel('Number of deaths')
    plt.legend()
    plt.savefig("bargraph.png")
    plt.show()

mydata= pd.read_csv(r'C:/Users/sahan/Desktop/visualisation project/HIV death.csv')
#dropping columns with less significance
mydata= mydata.drop(['IndicatorCode','Indicator', 'ValueType','Location type','Period type',
                     'Dim1 type','Dim1','Dim1ValueCode','Dim2 type','Dim2','Dim2ValueCode',
                     'Dim3 type','Dim3','Dim3ValueCode','DataSourceDimValueCode','DataSource',
                     'FactValueNumericPrefix','FactValueUoM','FactValueNumericLowPrefix',
                     'FactValueNumericHighPrefix','FactValueTranslationID','FactComments',
                     'Language','DateModified','Value','IsLatestYear'],axis=1)

#dropping rows with null values
new_data= mydata.dropna()
regions= new_data['ParentLocation'].unique()
#n is the number of regions present in the data
n= len(regions)
subplots()
top5_piechart()
multiline()
bar_graph()


