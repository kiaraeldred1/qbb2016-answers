#!/usr/bin/env python
"""
Usage: ./01timeCourse.py <metadata.csv> <ctab_dir>
 e.g. ./01-timecourse.py samples.csv ~dta/results/stringie
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_meta = pd.read_csv( sys.argv[1])
ctab_dir = sys.argv[2]

fem_Sxl = []

df_roi = df_meta[ "sex" ] == "female"
# check if it is a data frame: print type df_meta[ df_roi ]

for sample in df_meta[ df_roi ][ "sample" ]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi2 = df[ "t_name"] == "FBtr0331261"
    fem_Sxl.append( df[ df_roi2 ][ "FPKM" ].values )
    

# we just need: [1, 0, 10, 50, 100], a list of the mRNA abundances for one gene: sxl to be able to populate our plot

plt.figure()
plt.plot( fem_Sxl )
plt.show( )
#plt.savefig( "timecourse.png" )
#plt.close()

print "all finished"
