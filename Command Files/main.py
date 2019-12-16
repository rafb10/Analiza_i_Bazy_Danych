# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:36:38 2019
@author: RB
"""
import pandas as pd


data = pd.read_excel("dem_score.xlsx",index_col=0)
data = data.transpose()

data.to_csv("final_data.csv")
