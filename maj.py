# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:17:01 2018

@author: jnguyen3
"""

if __name__== "__main__":
    fname = r"C:\Users\jnguyen3\Downloads\rosalind_maj (1).txt"
    #brute force
    with open(fname) as f:
        header = next(f).split()
        lines = int(header[0])
        length = int(header[1])
        limit = int(length/2)
        output = []
        for line in f:
            val = -1
            numbers = set(line.split())
            for num in numbers:
                if line.split().count(num) > limit:
                    val = num
                    break
            print val
            output.append(val)
        print " ".join(str(x) for x in output)       
    