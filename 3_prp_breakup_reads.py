#!/usr/bin/env python2.7



import sys
import itertools
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import subprocess
import os



if len(sys.argv) is not 3:
    print "Usage: <filtered.fastq> <# of reads per file (int)>"
    sys.exit()

num_lines = sum(1 for line in open(sys.argv[1]))
lines_per_file = int(sys.argv[2])  

reads = open(sys.argv[1], "rU")
rf = FastqGeneralIterator(reads)

count = 0
initial_count = 0
line_list = []

for (title, seq, qual) in rf:
    count += 1
    #print count
    title = "@" + title
    if count in range(initial_count, (initial_count + lines_per_file)):
        
        
        
        line_list.append(title)
        line_list.append(seq)
        line_list.append("+")
        line_list.append(qual)
    else:
       
        initial_count += lines_per_file
        
        small_file = open(str(initial_count)+"batch.fastq", "w")
        for thing in line_list:
            
            print >>small_file, str(thing)
        del line_list[:]

