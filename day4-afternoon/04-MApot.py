#!/usr/bin/env python

""""

Funtion: transform ctab data to make an MA-plot. 


usage: ./03-histogram.py <datafile.ctab>

"""

#imports
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import data
df = pd.read_table( sys.argv[1] )
df2 = pd.read_table( sys.argv[2] )

# make a new list with log FPKM
df_roi = np.log( df[ "FPKM"] )
df2_roi = np.log( df2[ "FPKM"] )

m = (np.log2(df_roi)+1) - (np.log2(df2_roi)+1)
a = np.divide( ( (np.log2( df_roi )+1) + (np.log2( df2_roi )+1) ), 2 )

plt.figure()
plt.title( "MA Plot for SRR072893 and SRR072915")
plt.scatter( a, m, alpha = 0.1 )
plt.xlabel("A = 1/2 log2(SRR072893 * SRR072915)")             
plt.ylabel( "M= log2(SRR072893 / SRR072915)")
plt.savefig( "MAplot.png")
plt.close()