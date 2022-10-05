# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 09:09:00 2022

@author: spppy
"""

import pandas as pd
df=pd.read_csv("F:\project\python\Automobile_data.csv")
df.head(5)
print(df.head(5))
print(df.tail(5))
print(df.describe())
print(df.info())
print(type(df))
print(df.shape)
print(df.columns)