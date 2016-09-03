#!/usr/bin/env python

""""

Funtion: use two different ctab files to make an MA-plot of log(FPKM) values. 


usage: ./04-MAplot.py <datafile1.ctab> <datafile2.ctab>

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
df_roi = ( df[ "FPKM"] )+1
df2_roi = ( df2[ "FPKM"] )+1

m = (np.log2(df_roi)) - (np.log2(df2_roi))
a = np.divide( ( (np.log2( df_roi )) + (np.log2( df2_roi )) ), 2 )

plt.figure()
plt.title( "MA Plot for log(FPKM) of SRR072893 and SRR072915")
plt.scatter( a, m, alpha = 0.1 )
plt.xlabel("A = 1/2 log2(SRR072893 * SRR072915)")             
plt.ylabel( "M= log2(SRR072893 / SRR072915)")
plt.savefig( "MAplot.png")
plt.close()