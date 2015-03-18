#!/usr/bin/env python2.7

import sys
import itertools
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import subprocess
import os


if len(sys.argv) is not 2:
    print "command.py  <genome_name>"
    sys.exit()




root_dir = '.'
genome = sys.argv[1]
for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        if ".tar "  in file:
            subprocess.call(["tar", "-xzf", file])
        if ".tar.gz" in file:
            subprocess.call(["gunzip", file])
        if ".gz" in file:
            subprocess.call(["gunzip", file])
        else:
            pass
subprocess.call(["cat *.fastq > all_reads.fq"], shell = True)   

reads = open("all_reads.fq", "rU")
filteredReadPair1 = open(genome + "_filtered.fastq", "w")
f_iter1 = FastqGeneralIterator(reads)

for (title1, seq1, qual1) in f_iter1:
    count = 0
    tit = title1.split()
    head = tit[0]
    if ":N:" in title1:
        count = count + 1
    
    if "N" not in seq1:
        count = count + 1
   
    if count == 2:
    
        print >>filteredReadPair1, "@" + genome +"_"+ head + "_#0/1"
        print >>filteredReadPair1,  seq1
        print >>filteredReadPair1,  "+"
        print >>filteredReadPair1,  qual1 


filteredReadPair1.close()
reads.close()

