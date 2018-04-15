#!/usr/bin/env python3
import os
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
import argparse
import re
import subprocess


	
def ManualParse(fp):
	fasta_sequences = SeqIO.parse(open(fp),'fasta')
	for fasta in fasta_sequences:
		name, sequence = fasta.id, str(fasta.seq)
		print(name + "," + sequence + "," + "GO:0001539")
		
if __name__ == "__main__":

	p = argparse.ArgumentParser()
	p.add_argument("f_in", help = "Pass in a file")
	args = p.parse_args()

	ManualParse(args.f_in)


