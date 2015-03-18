#!/usr/bin/env python2.7

import sys
import os
import subprocess


if len(sys.argv) is not 2:
    print "Usage: reference_mapping_PL.py </path/reference.fasta>"
    
    
    sys.exit()
reference_fa = sys.argv[1]

subprocess.call(["maq" , "fasta2bfa", reference_fa, "reference.bfa"])
