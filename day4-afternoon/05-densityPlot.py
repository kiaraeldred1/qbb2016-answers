#!/usr/bin/env python

""""

Function: reate a histogram of the FPKM values for a ctab file

usage: ./03-histogram.py <datafile.ctab>

I could also try to make the plot a bit smaller so you can see all of the y axis lable.

I wanted to use seaborn but I couldn't figure out how to install it:

import seaborn as sns
data = df[ "FPKM" ]
sns.set_style('whitegrid')
sns.kdeplot(np.array(data), bw=0.5)
plt.show()

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
data = df[ "FPKM" ]
density = gaussian_kde(data)
xs = np.linspace(0,8,200)
density.covariance_factor = lambda : .5
density._compute_covariance()
plt.figure()
plt.plot(xs,density(xs))
plt.title( "Density plot of the FPKM values for SRR072893")
plt.ylabel( "Density" )
plt.savefig( "densityPlot.png" )
plt.close()



