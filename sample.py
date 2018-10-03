# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 12:24:51 2018

@author: Thinkpad
"""
# =============================================================================
# Write an algorithm to print out a line number for {1,2,3,..n}, 
# on each multiple of 3 print("Hello"); on each multiple of 7, print("World"); 
# if its a multiple of both 3 and 7, print("bingo")
# =============================================================================


import pandas as pd

#fileHandle = """
#Symbol,Last,Bid,Ask,Qty,Order Type
#ABC,53.0,51.1,53.1,100,Limit
#QtE,1.5,1.4,1.5,101,Market
#"""

#input_data = re.sub(r'\n', r',', fileHandle)   
#fields = input_data.split(',')          # Splits data into separate indices
#del fields[0]

data = pd.read_csv('input.csv')
#data = pd.to_numeric(data),errors=coerce)
# data = pd.DataFrame('fields')


NumberOfRows=data.shape[0]
NumberOfCols=6
for x in range(0, NumberOfRows):
    data.loc[x]=pd.to_numeric(data.loc[x],errors='coerce')



for i in range(0, NumberOfRows): 
    for j in range(0, NumberOfCols):
#for i in data:
        print(i)
        if data.iloc[i,j] == 'nan':
            break
        elif data.iloc[i,j]%3 == 0 and data.loc[i,j]%7 == 0:
            print("bingo")
        elif data.iloc[i,j]%3 == 0:
            print("Hello")
        elif data.iloc[i,j]%7 == 0:
            print("World")
