# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 16:21:54 2018

@author: jnguyen3
"""

from Bio import SeqIO

from collections import defaultdict

def grph(fasta, k):
    #open fasta file
    sequences = [x for x in SeqIO.parse(fasta,"fasta")]
    #nested for loop
    #for each sequence
    for seq in sequences:
        #check against every other sequence
        for seq2 in sequences:
            #if the same, skip
            if seq.id == seq2.id:
                continue
            #if the last k, are the same as the first k
            #print to output, or save
            if seq.seq[-k:] == seq2.seq[0:k]:
                print seq.id,seq2.id    
    return
    

#code from rosalind
def overlap(alist):
    prefixes = defaultdict(list)
    for name, code in alist:
        prefixes[code[:3]].append(name)
    for name, code in alist:
        suffix = code[-3:]
        for other in prefixes[suffix]:
            if other != name:
                print name, other 

if __name__ == "__main__":
    fasta = r"C:\Users\jnguyen3\Downloads\rosalind_grph (2).txt"
    k = 3    
    grph(fasta, k)