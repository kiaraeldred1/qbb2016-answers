#!/usr/bin/env python
"""

Function: Creates a graph of the rolling mean FPKM for two .ctab files. The differnet chromoromes will be ploted on seporate graphs

usage: ./plotFPKMbyPosition.py YOURPATH893/t_data.ctab YOURPATH15/t_data.ctab window_size

"""

# import all nessisary programs
import sys
import pandas as pd
import matplotlib.pyplot as plt

# import all nessisary files
df1_ctab = pd.read_csv(sys.argv[1], sep="\t")
df2_ctab = pd.read_csv(sys.argv[2], sep="\t")
size = int(sys.argv[3])

# make a list of chomosomes you want to look at 
chr_list = ["2L", "2R", "3L", "3R", "4", "X"]

# calculate the rolling mean of FPKMs
for entry in chr_list:
    df1_roi = df1_ctab["chr"] == entry
    df1_chrom = df1_ctab[df1_roi]
    smoothed1 = df1_chrom["FPKM"].rolling(size).mean()

    df2_roi = df2_ctab["chr"] == entry
    df2_chrom = df2_ctab[df2_roi]
    smoothed2 = df2_chrom["FPKM"].rolling(size).mean()
    
    
# this will make and lable all the graphs independely     
    plt.figure()
    plt.title( "Chromesome %s rolling average of transcripts (size = %s)" % (entry,size))
    plt.plot( smoothed1 )
    plt.plot( smoothed2 )
    plt.savefig( "lunchexercise2_%s.png" % (entry))
    plt.close()
    
    
    
