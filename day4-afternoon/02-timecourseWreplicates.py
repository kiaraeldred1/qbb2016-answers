#!/usr/bin/env python

"""
Function:

Usage: ./02-timecourseWreplicates.py <metadata.csv> <ctab_dir>
 e.g. ./02-timecourseWreplicates.py samples.csv ~dta/results/stringie

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_meta = pd.read_csv( sys.argv[1])
ctab_dir = sys.argv[2]
df_meta_rep = pd.read_csv( sys.argv[3])


fem_Sxl = []
mal_Sxl = []

fem_Sxl_rep = [ np.nan, np.nan, np.nan, np.nan ]
mal_Sxl_rep = [ np.nan, np.nan, np.nan, np.nan ]

#parse the date for femle
df_roi = df_meta[ "sex" ] == "female" # check if it is a data frame: print type df_meta[ df_roi ]
for sample in df_meta[ df_roi ][ "sample" ]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi2 = df[ "t_name"] == "FBtr0331261"
    fem_Sxl.append( df[ df_roi2 ][ "FPKM" ].values )
    
#parse for male
df_roi = df_meta[ "sex" ] == "male" # check if it is a data frame: print type df_meta[ df_roi ]
for sample in df_meta[ df_roi ][ "sample" ]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi2 = df[ "t_name"] == "FBtr0331261"
    mal_Sxl.append( df[ df_roi2 ][ "FPKM" ].values )

# and now the replicates

#parse for female replicate
df_roi = df_meta_rep[ "sex" ] == "female" # check if it is a data frame: print type df_meta[ df_roi ]
for sample in df_meta_rep[ df_roi ][ "sample" ]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi2 = df[ "t_name"] == "FBtr0331261"
    fem_Sxl_rep.append( df[ df_roi2 ][ "FPKM" ].values )

#parse for male replicate
df_roi = df_meta_rep[ "sex" ] == "male" # check if it is a data frame: print type df_meta[ df_roi ]
for sample in df_meta_rep[ df_roi ][ "sample" ]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi2 = df[ "t_name"] == "FBtr0331261"
    mal_Sxl_rep.append( df[ df_roi2 ][ "FPKM" ].values )
    
       
# we just need: [1, 0, 10, 50, 100], a list of the mRNA abundances for one gene: sxl to be able to populate our plot

#varibles for plot
labels = [ "10", "11", "12", "13", "14A", "14B", "14C", "14D" ]

# make the plot
plt.figure()
plt.title( "Sxl" )
plt.plot( fem_Sxl, color='red', linewidth=4)
plt.plot(fem_Sxl_rep, color='red', linestyle='none', marker='o',markerfacecolor='red', markersize=10)
plt.plot( mal_Sxl, color='blue', linewidth=4)
plt.plot(mal_Sxl_rep, color='blue', linestyle='none', marker='o',markerfacecolor='blue', markersize=10)
plt.xticks( [0,1,2,3,4,5,6,7], labels )
plt.xlabel( "Stage of Development")
plt.ylabel( "mRNA abundance (FPKM)")
plt.legend( ['female', 'female replicate', 'male', 'male replicate'], loc='upper left')
plt.savefig( "timecourse.png" )
plt.close()


