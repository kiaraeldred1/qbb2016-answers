#!/usr/bin/env python

""""

function: make a log scaled box plot of the FPKM values from two files.
Usage: lunchBoxPlot.py file_1.ctab file_1.ctab

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_ctab = pd.read_csv( sys.argv[1], sep = "\t" )
df2_ctab = pd.read_csv( sys.argv[2], sep = "\t" )

df_roi = df_ctab[ "gene_name" ] == "Sxl"
df_sxl = df_ctab[ df_roi ]
df_roi2 = df_sxl[ "FPKM" ] > 0
df_sxl_Fsort = df_sxl[ df_roi2 ]

#print df_sxl_Fsort



df2_roi = df2_ctab[ "gene_name" ] == "Sxl"
df2_sxl = df2_ctab[ df_roi ]
df2_roi2 = df2_sxl[ "FPKM" ] > 0
df2_sxl_Fsort = df2_sxl[ df_roi2 ]

#print df2_sxl_Fsort

#============================================================#
# CREATE SOME PLOTS

# Extract the first feature from the dataset

names = [ "SRR072893", "SRR07295" ]

plt.figure()                       # Open a blank canvas
plt.title("Sxl Transcripts in Samples") # Add a title to the top
plt.boxplot([df_sxl_Fsort[ "FPKM" ], df2_sxl_Fsort[ "FPKM" ] ], labels=names )
    # ...of the values for each SAMPLE
	#labels=samples,                # ...with the species names as labels
	#)
plt.yscale( 'log' )
plt.xlabel("Samples")              # Label the x-axis
plt.ylabel( "log10(FPKM) of Sxl")
plt.savefig("day4-lunch-1.png")   # Save the plot
plt.close()                        # Close the canvas


