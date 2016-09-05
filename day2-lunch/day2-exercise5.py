#!/usr/bin/env python

"""

Function: calculate average MAPQ score

Usage: ./day2-exercise#4.py <samfile>

"""

import sys

data = open('samfile.sam')

count1 = 0
count2 = 0

for line in data:
    if line.startswith( "@" ):
        continue       
    # skip the header
    fields = line.rstrip( "\r\n" ).split( "\t" )
    #strip the feilds in each line and split them delimited by tabs
    for field in fields[4]:
        count1 += int(field)
        count2 += 1
            
print "Total MAPQ Score = " 
print count1
print "Total number of scores = " 
print count2
print "Average MAPQ Score = " 
print count1/count2