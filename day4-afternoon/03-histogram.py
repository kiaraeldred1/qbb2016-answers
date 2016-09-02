#!/usr/bin/env python

""""

Function: reate a histogram of the FPKM values for a ctab file

usage: ./03-histogram.py <datafile.ctab>

"""

#imports
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import data
df = pd.read_table( sys.argv[1])

# filter out zero-values
df_roi = df[ "FPKM" ] > 0
df_filter = df[ df_roi ]


plt.figure()
plt.title( "Histogram of SRR072893 FPKM Values")
plt.hist( np.log( df_filter[ "FPKM" ] ) )
plt.savefig( "histSRR072893.png")
plt.close()