# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 15:38:12 2018

@author: jnguyen3
"""

'''
cons
'''

from Bio import SeqIO

def cons(fasta):
    #open fasta file, and save sequences
    sequences = [seq_record.seq for seq_record in SeqIO.parse(fasta,"fasta")]
    
    #print sequences
    #unzip with *
    #creates a list of tuples, each tuple represents a position in the sequences
    #each item in the tuple represents the letter at that sequence
    matrix = zip(*sequences)  
    #print matrix
    
    #create a profile matrix
    #map takes a function, and applies it to every element in a list/iterable
    #lambda forms a function
    #   in this case, it takes an x, and returns a dict composed of base, and count of base
    #we end up with a list of dicts, that are composed of base:count(base)
    profile_matrix = map(lambda x:dict((base, x.count(base)) for base in "ACGT"), matrix)
    print profile_matrix
    
    #form a consensus, by selecting the max element of each dict
    #consensus is a list of which key had the highest count    
    consensus = [max(x,key = x.get) for x in profile_matrix]
    #print consensus    
    
    #print to the required output    
    #'''    
    print "".join(consensus)
    for base in "ACGT":
        print base + ":",
        for x in profile_matrix:
            print x[base],
        print ""
    #'''
    return

if __name__ == "__main__":
    fasta = r"C:\Users\jnguyen3\Downloads\rosalind_cons (4).txt"
    cons(fasta)