#!/usr/bin/env python

"""

Function: for first ten alignments, print just the chromosme column

Usage: ./day2-exercise#4.py <samfile>

"""

import sys

data = open('samfile.sam')

count = 0

for line in data:
    if line.startswith( "@" ):
        continue       
    # skip the header
    fields = line.rstrip( "\r\n" ).split( "\t" )
    #strip the feilds in each line and split them delimited by tabs
    for field in fields[2]:
        if count < 10:
            count += 1
            print field
        