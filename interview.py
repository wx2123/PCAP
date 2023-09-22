# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:15:37 2022

@author: xuewu
"""

x=[i for i in range(5)]

def xyz(a):
    pass

import array as arr
My_Array=arr.array('i',[1,2,3,4,5])
My_Array[::-1]

My_Array[::-2]


stg='ABCD'
print(stg.lower())

if 'a' is "a":
    print(2)


a=arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
print(a.pop())
print(a.pop(3))
a.remove(1.1)
print(a)    
#a.remove('d')
print(a)



import pandas as pd

data_1 = {'product': ['computer','monitor','printer','desk'],
                   'price_1': [1200,800,200,350]
                   }
df1 = pd.DataFrame(data_1)
print(df1)

data_2 = {'product': ['computer','monitor','printer','desk'],
                    'price_2': [900,800,300,350]
                    }
df2 = pd.DataFrame(data_2)
print (df2)


import datacompy
compare = datacompy.Compare(
df1,
df2,
join_columns='product', #You can also specify a list of columns
abs_tol=0.0001,
rel_tol=0,
df1_name='original',
df2_name='new')

print(compare.report())


df1
df1.loc[3, 'price_1']
df1.loc[:, 'price_1']

df1.iloc[3,1]


import numpy as np

images = np.ones((10000,10000,10000))
images


import dask.array as da

images = da.ones((10000,10000,10000))
images
