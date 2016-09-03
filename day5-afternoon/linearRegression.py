#!/usr/bin/env python

""" 

Function: calculate the linear regression of fpkm values compared to known histone modifications wihin promotor regions

Usage: ./linearRegression.py <file_name.bed> <output_from_Big_Wig_file>

"""

#import packages
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

#import data
df_fpkm = pd.read_table( sys.argv[1], header= None)
df_mark = pd.read_table( sys.argv[2], header= None)

newDataFrame = df_fpkm.merge(df_mark, left_on=0, right_on=0)

#print newDataFrame
#we want column 4 from the bw output-y and 0 fpkm-x


# Fit regression model
results = sm.OLS( newDataFrame[2], newDataFrame[5] ).fit()

# Inspect the results
print results.summary()








