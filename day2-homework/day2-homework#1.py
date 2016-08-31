#!/usr/bin/env python

"""
This script will parse out a flybase file into one column containing the FlyBAse ID and another with the Uniport ID
To use this script, enter the folowing into bash window:
./day2-homework#1.py < fly.txt | cat > day2-homwork#1.out
fly.txt is the file you are reading, and the new file will be writen in day2-homwork#1.out 
"""

import sys

drome_list = []

for line in sys.stdin:
    if "DROME" in line:
        feilds = line.rstrip( "\r\n" ).split( )
    #strip the feilds in each line and split them delimited by blank space
        numcol = len(feilds)
        if numcol == 4:
            drome_list.append( feilds [2:4] )
        if numcol == 5:
            drome_list.append( feilds [3:5])
    
print '\n'.join(map('\t'.join,drome_list))
