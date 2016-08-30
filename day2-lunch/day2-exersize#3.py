#!/usr/bin/env python

import sys

count = 0 
for line in sys.stdin:
    if line.startswith( "@" ):
        continue         
    # skip the header
    feilds = line.rstrip( "\r\n" ).split( "\t" )
    #strip the feilds in each line and split them delimited by tabs
    for field in feilds[12:]:
        subfields = field.split( ":" )
        if subfields [0] == "NH":
            if subfields [2] == "1":
                count+=1
                
print count