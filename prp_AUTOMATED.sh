#!/bin/bash
if [ -z "$*" ]; then echo "Usage:  arg1 = genome_name  arg2 = /path/reference.fasta arg3 = number or reads per small file"; fi


python2.7 1_reference_fasta_2_maq_bfa.py   $2  #</path/reference.fasta>
python2.7 2_se_fastq_processor.py  $1 #<genome name>
python2.7 3_prp_breakup_reads.py    $1"_filtered.fastq" $3   # <filtered.fastq> <# of reads per file (int)>
python2.7 4_prp_read_convertor.py 
python2.7 5_prp_maq_assemble.py



