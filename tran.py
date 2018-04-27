# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:03:28 2018

@author: jnguyen3
"""

from Bio import SeqIO
import sys


PUR = ["A","G"]
PYR = ["C","T"]

def tran(fname):
    records = list(SeqIO.parse(fname,"fasta"))
    sequences = [x.seq for x in records]
    transitions = 0
    transversions = 0
    for i in range(len(sequences[0])):
        if sequences[0][i] == sequences[1][i]:
            continue
        if sequences[0][i] in PUR:
            if sequences[1][i] in PUR:
                transitions += 1
            else:
                transversions += 1
        else:
            if sequences[1][i] in PUR:
                transversions += 1
            else:
                transitions += 1
    print transitions
    print transversions
    print float(transitions)/transversions    
    
if __name__ == "__main__":
    fname = r"C:\Users\jnguyen3\Downloads\rosalind_tran (1).txt"
    tran(fname)