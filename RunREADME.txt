
Instructions for single end assembly of Illumina data

This script uses MAQ (http://maq.sourceforge.net/maq-man.shtml,http://maq.sourceforge.net/maq-manpage.shtml, http://maq.sourceforge.net/)   

MAQ Reference:
Li H, Ruan J, Durbin R. 2008. Mapping short DNA sequencing reads and calling variants using mapping quality scores. Genome Research 18:1851–1858.

Intended for reads no longer 



Scripts:

1_reference_fasta_2_maq_bfa.py #<reference.fasta>
    Python script that uses Maq to convert reference genome.fasta to binary genome.bfa



2_se_fastq_processor.py #<single-reads.fastq><genome_name>
    
    -unarchives all read files in .gz or .tar
    -cats all unarchive.fastq files together
    -filters for 'N' or reads that are flagged by Illumina filter
    
3_prp_breakup_reads.py #<filtered.fastq> <# of reads per file (int)>
    -breaks up reads into 2 million read files
    -Maq works better if you dont feed it more than 2million reads at a time
        
        
4_prp_read_convertor.py #Just run it in the same directory
    -converts read files to binary reads.bfq
    
5_prp_maq_assemble.py #Just run it in the same directory
    -maps reads to reference and produces a draft with quality for each position in draft.fastq format




    
    
    
    
    
    
    
    
