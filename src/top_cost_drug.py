# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:35:51 2018

@author: Thinkpad
"""
import re
import numpy as np

input_file = "/input/itcont.txt"
fileHandle = open('input_file', 'r') 

#fileHandle = """
#id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
#1000000001,Smith,James,AMBIEN,100
#1000000002,Garcia,Maria,AMBIEN,200
#1000000003,Johnson,James,CHLORPROMAZINE,1000
#1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
#1000000005,Smith,David,BENZTROPINE MESYLATE,1500
#"""
input_data = re.sub(r'(\n)', r',\1', fileHandle)   
fields = input_data.split(',')    
del fields[0]

NumberOfRows = round(len(fields)/5)
NumberOfCols = 5
length_of_fields=len(fields)

# Expected output: drug_name,number_of_prescribers,total_cost
# drug_name at indices 3 (title), 8, 13, 18, 23, 28
# drug_cost at indices 4 (title), 9, 14, 19, 24, 29


outputfile = open('/output/top_cost_drug.txt','w') 

# get list of drug names
i=8
j=0
drug_name_list=list()
drug_name_indices=list()
while i<=length_of_fields:
    drug_name_list.append(fields[i])
    drug_name_indices.append(i)
    i=i+5;
    j=j+1;
    
# find unique names (same as drug_name_list but without repetition)
    
unique_drug_list = list()

     
 # traverse for all elements
for x in drug_name_list:
        # check if exists in unique_name_list or not
   if x not in unique_drug_list:
       unique_drug_list.append(x)

i=0
j=0
number_of_unique_drugs=len(unique_drug_list)
unique_cost_list=[0]*number_of_unique_drugs
number_of_prescribers = [0]*number_of_unique_drugs

# unique_cost_list = list(0 for y in xrange(0, number_of_unique_drugs))


#while i<len(drug_name_list):   
#    while j<number_of_unique_drugs:
#        if drug_name_list[i]==unique_drug_list[j]:
#            drug_name_index=drug_name_indices[i]
#            cost_of_drug=int(fields[drug_name_index+1])
#            unique_cost_list[j]=int(unique_cost_list[j])+cost_of_drug
#            number_of_prescribers[j]=number_of_prescribers[i]+1
#        j=j+1
#    i=i+1

while j<number_of_unique_drugs:
    while i<len(drug_name_list):   
        if drug_name_list[i]==unique_drug_list[j]:
            drug_name_index=drug_name_indices[i]
            cost_of_drug=int(fields[drug_name_index+1])
            unique_cost_list[j]=int(unique_cost_list[j])+cost_of_drug
            number_of_prescribers[j]=number_of_prescribers[j]+1
        i=i+1
    j=j+1
   
# print output values
counter=0
print("drug_name,number_of_prescribers,total_cost \n")
while counter<number_of_unique_drugs:
    print(unique_drug_list[counter], number_of_prescribers[counter], unique_cost_list[counter])
    print("\n")
    counter=counter+1
        
    
#    drug_name,num_prescriber,total_cost
#CHLORPROMAZINE,2,3000
#BENZTROPINE MESYLATE,1,1500
#AMBIEN,2,300
        
        #also check prescriber first and last name
    
 #   keys   = ['A', 'B', 'C', 'A', 'B', 'C']
 #   vals = [ 1,   2,   3,   4,   5,   6 ]

#i = 1
#while i <= NumberOfRows:   # compare drug names to see if any are the same. If so, output that ID and other info.
#    for j in range((i-1),-1,-1):                                             # for(j=i; j>=0; j=j-1)
#        if fields[i+7] == fields[j][]:
#
#result = {}
#for key, val in zip(keys, vals):
#    if key not in result:
#        result[key] = 0
#    result[key] += val
#print(result)