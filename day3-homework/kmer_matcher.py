#!/usr/bin/env python

"""
Read sequences from a fasta file,  
index each k-mer as a key in a dictionary that will refference the gene and position it occupys 
Then read k-mers in a fasta file of a genome and see if any of the indexed kmers match

the script will iterate through each gene in the orinal fatsa file sequentaly, 
for each match it will print:
target_sequence_name    target_start    query_start k-mer 

k-mer is defined as 11 in script

usage: kmer_matcher.py frirst_file_of_genes.fa genmoe_file.fa

"""

import sys, fasta

#command line argument

k = int( 11 )

kmer_position = {}

target = sys.argv[1]
query = sys.argv[2]

for ident, sequence in fasta.FASTAReader( open( target ) ):
    kmer_position = {}
    sequence = sequence.upper()
    for i in range( 0, len( sequence ) - k ):
        kmer = sequence[ i : i+k ]
        if kmer not in kmer_position:
            kmer_position[ kmer ] = []
        kmer_position[ kmer ].append(i)
        
    for fly, genome in fasta.FASTAReader( open( query ) ):
        genome = genome.upper()
        for i in range( 0, len( genome ) - k ):
            kmercompare = genome[ i : i+k ]
            if kmercompare in kmer_position:
                print ident, kmer_position[ kmercompare ][0], i, kmercompare
