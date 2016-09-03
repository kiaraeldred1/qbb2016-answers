#!/usr/bin/env  python
"""

Function: find the promotor regions of all genes listed in the ctab data output file
this is defined as 500 bps infront of and behind the start site possition
Output: tab delimited bed file containing chromomsoem, start, end, and gene name of the promotor region in a .bed file

Usage: ./findRegion.py <ctab_file>

"""


import sys
import pandas as pd
import numpy as np

#import files
df = pd.read_table( sys.argv[1])

#cut out shitty chromosmes
df_trans = df.loc[df["chr"].isin(["2L", "2R", "3L", "3R", "4", "X"])]

#make the plus strands
df_roi = df_trans[ "strand" ] == "+"
df_pls = df_trans[ df_roi ]

#extend the start possition for plus strand
df_pls["start"] = df_pls[ "start" ] - 500
df_pls["end"] = df_pls["start"]+ 1000

#make a plus strand data frame
selected = ["chr", "start","end","t_name"]
df_pls_bed = pd.DataFrame(df_pls, columns = selected)

#---- and now minus

#make the minus strands
df_roi = df_trans[ "strand" ] == "-"
df_mins = df_trans[ df_roi ]

#extend the start possition for minus strand
df_mins["end"] = df_mins[ "end" ] + 500
df_mins["start"] = df_mins["end"]- 1000

#make a minus strand data frame
selected = ["chr", "start","end","t_name"]
df_mins_bed = pd.DataFrame(df_mins, columns = selected)

#---- name a new file

# make a new concatinated file
frames = [ df_pls_bed, df_mins_bed ]
merged_bed = pd.concat(frames)

#save tab delimited file
merged_bed.to_csv("promoter.bed", sep='\t', index = False, header= False)

#chromosome start end t_name

#numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')[source]