# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:36:38 2019

@author: RB
"""
import pandas as pd

#data = pd.read_csv("dem_score.csv");
data = pd.read_excel("dem_score.xlsx")
data = data.transpose()

data.to_csv("final_data.csv")
#df_new = pd.read_csv('final_data.csv').drop(['unnamed 0'],axis=1)
