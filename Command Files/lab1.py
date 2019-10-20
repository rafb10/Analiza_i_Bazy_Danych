# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:36:38 2019

@author: student210
"""
import pandas as pd

data = pd.read_excel("dem_score.xlsx", index = None)
data = data.transpose()

#data = pd.read_csv("dem_score.csv", index = None)
#data = data.transpose()

print(data)

data.to_csv("final_data.csv")
