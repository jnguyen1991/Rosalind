# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:50:54 2018

@author: jnguyen3
"""

from Bio import SeqIO

def lexf(output, alpha):
    new_output = []
    for i in output:
        for j in alpha:
            new_output.append(i + j)
    return new_output
            
def gen_kmer_dict(alpha=["A","C","G","T"],n=4):
    output = alpha
    while n > 1:
        output = lexf(output,alpha)
        n-= 1
    return {k:0 for k in output}, output
    
def find_kmer(seq_path):
    seq_rec = [i for i in SeqIO.parse(seq_path, "fasta")]
    seq = seq_rec[0].seq
    output_dict, output = gen_kmer_dict()
    for i in range(len(seq)):
        if i+4>len(seq):
            continue
        output_dict[str(seq[i:i+4])] += 1
    ans = [str(output_dict[x]) for x in output]
    print " ".join(ans)

fpath = r"C:\Users\jnguyen3\Downloads\rosalind_kmer (1).txt"
find_kmer(fpath)

