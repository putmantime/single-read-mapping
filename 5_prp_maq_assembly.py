#!/usr/bin/env python2.7

import sys
import os
import subprocess


if len(sys.argv) is not 1:
    print "Usage: just run it"
    sys.exit()



root_dir = '.'
count = 0
for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        if ".bfa" in file:
            reference = file
        if ".bfq" in file:
            count = count + 1
            file_name = (str(count),"_file.map")
            name = "".join(file_name)
            open(name, "w")
            fastq =  os.path.join(directory, file)
            subprocess.call(["maq", "match",name, reference, file])
        
subprocess.call(["maq mapmerge out.map *.map"], shell = True)
subprocess.call(["maq","assemble", "out.cns", reference,"out.map"])
subprocess.call(["maq cns2fq out.cns > draft_cns.fq"], shell = True)
