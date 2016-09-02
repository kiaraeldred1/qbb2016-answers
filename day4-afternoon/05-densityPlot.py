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
from scipy.stats import gaussian_kde

#import data
df = pd.read_table( sys.argv[1])

#Plot data
data = np.log(df[ "FPKM" ]+1)
density = gaussian_kde(data)
xs = np.linspace( np.min(data), np.max(data) , 1000)
density.covariance_factor = lambda : .5
density._compute_covariance()
plt.figure()
plt.plot(xs,density(xs))
plt.title( "Density plot of the FPKM values for SRR072893")
plt.ylabel( "Probability Density" )
plt.xlabel( "log(FPKM)" )
plt.savefig( "densityPlot.png" )
plt.close()



