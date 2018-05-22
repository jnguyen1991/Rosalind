# -*- coding: utf-8 -*-
"""
Created on Wed May 02 11:27:32 2018

@author: jnguyen3
"""

from math import log10

def prob(seq, gc_con):
    output = []
    gc_con = [float(x) for x in gc_con.split()]
    #kind of hacky, ordereddict is probably better
    #could use G and C together, instead of separate keys
    gc_dict = [{x:{"G":x/2,"C":x/2,"A":(1-x)/2,"T":(1-x)/2}} for x in gc_con]
    for table in gc_dict:
        for i in table:
            total = 0
            for x in seq:
                total += log10(table[i][x])
            output.append(total)
    return " ".join([str(x) for x in output])

with open(r"C:\Users\jnguyen3\Downloads\rosalind_prob.txt") as fhand:
    seq = fhand.next().strip()
    gc_con = fhand.next().strip()
    print prob(seq, gc_con)    
    

            