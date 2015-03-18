#!/usr/bin/env python2.7

import sys
import os
import subprocess


if len(sys.argv) is not 1:
    print "Usage: run in directory with broken up read files"
    sys.exit()
    


root_dir = '.'
count = 0
for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        if "batch" in file:
            count = count + 1
           
            file_name = (str(count),"_file.bfq")
            name = "".join(file_name)
            open(name, "w")
            fastq =  os.path.join(directory, file)
            subprocess.call(["maq", "fastq2bfq", file, name])
        
