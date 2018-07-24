# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:52:48 2018

@author: Thinkpad
"""

import pandas as pd

input_file = "./input/itcont.txt"
df = pd.read_csv(input_file)

#fileHandle = """
#id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
#1000000001,Smith,James,AMBIEN,100
#1000000002,Garcia,Maria,AMBIEN,200
#1000000003,Johnson,James,CHLORPROMAZINE,1000
#1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
#1000000005,Smith,David,BENZTROPINE MESYLATE,1500
#"""
#
#input_data = re.sub(r'(\n)', r',\1', fileHandle)   
#fields = input_data.split(',')    
#del fields[0]
#
#
#df = pd.DataFrame(fields)

df.groupby("drug_name").drug_cost.agg(["count", "sum"]).to_csv("./output/top_cost_drug.txt")