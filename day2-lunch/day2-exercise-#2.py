#!/usr/bin/env python

import sys

count = 0 
for dog in sys.stdin:
    if dog.startswith( "@" ):
        continue         
    # skip the header
    feilds = dog.rstrip( "\r\n" ).split( "\t" )
    #strip the feilds in each line and split them delimited by tabs
    for field in feilds[12:]:
        subfields = field.split( ":" )
        if subfields [0] == "NM":
            if subfields [2] == "0":
                count+=1
                
print count