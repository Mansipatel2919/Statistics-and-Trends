# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 06:02:40 2022

@author: Lenovo
"""
#importing libraries
import pandas as pa
import matplotlib.pyplot as pyp
import numpy as n
"""table plot"""
table_file=pa.read_csv("Electricity consumtion.csv")
dataframe=pa.DataFrame(table_file)

create_table=table_file.iloc[[17,33,39,44,49,79,255],:]
print(create_table)

"""
                      #BAR GRAPH 1
"""
#read csv
df_= pa.read_csv("ELECTRICITY HYDRO.CSV")
print(df_)
#transpose the file 
def transpose(df_):
    result=df_
    print(result )
#dropping the columns 
columns_drop=df_.drop(['Country Code','Indicator Name','Indicator Code'],axis=1)
print(columns_drop)
group = df_.groupby("Country Name").sum()
print(group)
#selecting the rows 
select_row=columns_drop.iloc[[7,20,25,30,35,65,71,236],:]
print(select_row)
#removing NaN's
null_drop=select_row.dropna()
print(null_drop)
#setting the index
col=(select_row["Country Name"])

x=n.arange(len(col))

m1=(select_row["1971"])
m2=(select_row["1975"])
m3=(select_row["1980"])
m4=(select_row["1985"])
m5=(select_row["1990"])
m6=(select_row["1995"])
m7=(select_row["2000"])
#plotting the bar graph 
pyp.figure()
pyp.title("Production From Hydroelecctricity Sources (% of total)")
pyp.bar(x-0.2,m1,0.1,label='1971')
pyp.bar(x-0.1,m2,0.1,label='1975')
pyp.bar(x+0,m3,0.1,label='1980')
pyp.bar(x+0.1,m4,0.1,label='1985')
pyp.bar(x+0.3,m5,0.1,label='1990')
pyp.bar(x+0.4,m6,0.1,label='1995')
pyp.bar(x+0.2,m7,0.1,label='2000')
pyp.xticks(x,col,rotation=45)
pyp.xlabel("Countries")
pyp.ylabel("(% of total)")
pyp.legend(bbox_to_anchor=(1.04,0.5),loc="center left")
pyp.show()


"""
                    BAR GRAPH 2
"""
#read csv file 
df_energy = pa.read_csv("COAL.CSV")
print(df_energy)
#dataframe transpose 
def transpose(df_energy):
    result=df_energy
    print(result )
#dropping the files which are not being used 
columns_drop=df_energy.drop(['Country Code','Indicator Name','Indicator Code','2012','2013','2015','2014','2016','2017','2018','2019'],axis=1)
print(columns_drop)
#selecting the rows  which are going to plot
select_row=columns_drop.iloc[[5,16,19,24,29,59,65,230],:]
print(select_row)
#remove Nan
null_drop=select_row.dropna()
print(null_drop)
#setting the index
indexing=null_drop.set_index("Country Name")
print(indexing)
col=(select_row["Country Name"])
#arranging the axis 
x=n.arange(len(col))
r1=(select_row["1971"])
r2=(select_row["1975"])
r3=(select_row["1980"])
r4=(select_row["1985"])
r5=(select_row["1990"])
r6=(select_row["1995"])
r7=(select_row["2000"])
#plotting bar graph 
pyp.figure()
pyp.title("Production From Coal Sources (% of total)")
pyp.bar(x-0.2,r1,0.1,label='1971')
pyp.bar(x-0.1,r2,0.1,label='1975')
pyp.bar(x+0,r3,0.1,label='1980')
pyp.bar(x+0.1,r4,0.1,label='1985')
pyp.bar(x+0.3,r5,0.1,label='1990')
pyp.bar(x+0.4,r6,0.1,label='1995')
pyp.bar(x+0.2,r7,0.1,label='2000')
pyp.xticks(x,col,rotation=45)
pyp.xlabel("Countries")
pyp.ylabel("(% of total)")
#bbox_to_anchor to place legend outside the axes such that the center left 
#corner of the legend is at position
pyp.legend(bbox_to_anchor=(1.04,0.5),loc="center left")
pyp.show()

"""
               #  LINE GRAPH 1
"""
#opening the csv file in reading using function 
with open("AGRICULTURE NITROUS OXIDE.CSV", 'r') as df_methane:
          print(df_methane)
#read the file using pandas 
df_NO= pa.read_csv("AGRICULTURE NITROUS OXIDE.CSV")
print(df_methane)
#dropping the columns which are not needed 
df_NO=df_NO.drop(['Country Code','Indicator Code','Indicator Name','1974','1975','1976','1977','1978','1979','1980','1981','1982',
    '1983','1984','1985','1986','1987','1988','1989','1990'],axis=1)
#replacing the Nans 
df_NO= df_NO.replace('..', n.NaN)
#transpose the data
df_transpose= pa.DataFrame.transpose(df_NO)
print(df_transpose)
#create header
header = df_transpose.iloc[0].values.tolist()
df_transpose.columns = header
print(df_transpose)
#removing the first two rows
df_transpose = df_transpose.iloc[2:]
print(df_transpose)
#notna used to returns a dataframe object where all the values are replaced with boolean value
df_transpose = df_transpose[df_transpose["Australia"].notna()]
df_transpose = df_transpose[df_transpose["Brazil"].notna()]
df_transpose= df_transpose[df_transpose["Canada"].notna()]
df_transpose= df_transpose[df_transpose["China"].notna()]
df_transpose= df_transpose[df_transpose["Finland"].notna()]
df_transpose= df_transpose[df_transpose["United States"].notna()]
df_transpose= df_transpose[df_transpose["Tanzania"].notna()]
print(len(df_transpose))
#to get types of individual column
df_transpose["Australia"] = pa.to_numeric(df_transpose["Australia"])
df_transpose["Brazil"] = pa.to_numeric(df_transpose["Brazil"])
#finding the average of the below  plotted countries
print("average of :-")
print("Australia")
print(df_transpose["Australia"].mean())
print("Brazil")
print(df_transpose["Brazil"].mean())
print("Canada")
print(df_transpose["Canada"].mean())
print("china")
print(df_transpose["China"].mean())
print("finland")
print(df_transpose["Finland"].mean())
print("United States")
print(df_transpose["United States"].mean())
print("Tanzania")
print(df_transpose["Tanzania"].mean())
# convert index to int
df_transpose.index = pa.to_numeric(df_transpose.index)
#plotting the line graph 
pyp.figure()
pyp.title("Agricultural nitrous oxide (thousand metric tons of CO2 equivalent)")
pyp.grid()
pyp.plot(df_transpose.index, df_transpose["Australia"], label="Australia",linestyle='dashed')
pyp.plot(df_transpose.index, df_transpose["Brazil"], label="Brazil",linestyle='dashed')
pyp.plot(df_transpose.index, df_transpose["Canada"], label="Canada",linestyle='dashed')
pyp.plot(df_transpose.index, df_transpose["China"], label="China",linestyle='dashed')
pyp.plot(df_transpose.index, df_transpose["Finland"], label="Finland",linestyle='dashed')
pyp.plot(df_transpose.index, df_transpose["United States"], label="United States",linestyle='dashed')
pyp.plot(df_transpose.index, df_transpose["Tanzania"], label="Tanzania",linestyle='dashed')
pyp.xlabel("year")
pyp.ylabel("(thousand metric tons of CO2)")
pyp.legend(bbox_to_anchor=(1.04,0.5),loc="center left")
pyp.show()

"""
                  # LINE GRAPH 2
""" 
#opening the file in reading mode
with open("AGRICULTURE METHANE.CSV", 'r') as df_methane:
          print(df_methane)
#read csv file         
df_methane=pa.read_csv ("AGRICULTURE METHANE.CSV") 

#dropping the columns  which are not being used 
df_methane=df_methane.drop(['Country Code','Indicator Code','Indicator Name','1974','1975','1976','1977','1978','1979','1980','1981','1982',
    '1983','1984','1985','1986','1987','1988','1989','1990'],axis=1)
print(df_methane)
#replacing the Nan's
df_hydro = df_methane.replace('..', n.NaN)
#transpose the  data
df_transpose= pa.DataFrame.transpose(df_methane)
print(df_transpose)
#creating the header 
header = df_transpose.iloc[0].values.tolist()
df_transpose.columns = header
print(df_transpose)
#Remove the first two lines
df_transpose = df_transpose.iloc[2:]
print(df_transpose)
#Remove NaN entriesfor the below countries 
print(len(df_transpose))
df_transpose = df_transpose[df_transpose["Australia"].notna()]
df_transpose = df_transpose[df_transpose["Brazil"].notna()]
df_transpose= df_transpose[df_transpose["Canada"].notna()]
df_transpose= df_transpose[df_transpose["China"].notna()]
df_transpose= df_transpose[df_transpose["Colombia"].notna()]
df_transpose= df_transpose[df_transpose["United Kingdom"].notna()]
df_transpose= df_transpose[df_transpose["Tanzania"].notna()]
print(len(df_transpose))
#to get types of individual column
df_transpose["Australia"] = pa.to_numeric(df_transpose["Australia"])
df_transpose["Brazil"] = pa.to_numeric(df_transpose["Brazil"])
print(df_transpose["Australia"])
print(df_transpose["Brazil"])
print("Median of :-")
print("Australia")
print(df_transpose["Australia"].median())
print("Brazil")
print(df_transpose["Brazil"].median())
print("Canada")
print(df_transpose["Canada"].median())
print("china")
print(df_transpose["China"].median())
print("finland")
print(df_transpose["Finland"].median())
print("United States")
print(df_transpose["United States"].median())
print("Tanzania")
print(df_transpose["Tanzania"].median())
# convert index to int
df_transpose.index = pa.to_numeric(df_transpose.index)
#plotting the figure
pyp.figure()
pyp.title("Agricultural methane emissions (thousand metric tons of CO2 equivalent)")
pyp.grid()
pyp.plot(df_transpose.index, df_transpose["Australia"], label="Australia")
pyp.plot(df_transpose.index, df_transpose["Brazil"], label="Brazil")
pyp.plot(df_transpose.index, df_transpose["Canada"], label="Canada")
pyp.plot(df_transpose.index, df_transpose["China"], label="China")
pyp.plot(df_transpose.index, df_transpose["Finland"], label="Finland")
pyp.plot(df_transpose.index, df_transpose["United States"], label="United States")
pyp.plot(df_transpose.index, df_transpose["Tanzania"], label="Tanzania")
pyp.xlabel("year")
pyp.ylabel("(thousand metric tons of CO2 equivalent)")
pyp.legend(bbox_to_anchor=(1.04,0.5),loc="center left")
pyp.show()

