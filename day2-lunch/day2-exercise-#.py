#!/usr/bin/env python

import sys

count = 0 
for line in sys.stdin:
    if line.startswith( "@" ):
        continue         
    # skip the header
    feilds = line.rstrip( "\r\n" ).split( "\t" )
    #strip the feilds in each line and split them delimited by tabs
    if feilds [2] == "*" :
        continue 
    # skip anything that is not alinged to the genome
    else: 
        count+=1

print count
    
    
    
    #convert and conpute length
    #length = int( feilds[4] ) - int( feilds[3] )
    # Write out with new field tab separated
    #feilds.append( str(length) )
    #print "\t".join( feilds )