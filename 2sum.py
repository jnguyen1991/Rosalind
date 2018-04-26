# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 14:54:56 2018

@author: jnguyen3
"""

if __name__ == "__main__":
    fname = r"C:\Users\jnguyen3\Downloads\rosalind_2sum (5).txt"
    with open(fname) as fhand:
        length = int(fhand.next().split()[1])
        for line in fhand:
            a,b = 0,0
            lst = [int(x) for x in line.split()]
            for i in range(length):
                if -lst[i] in lst[i+1:]:
                    val = -lst[i]
                    val_index = lst[i+1:].index(val)+i+1
                    if i == val_index:
                        continue
                    else:
                        a,b = i+1, val_index+1
                        break
                        #print i+1, val_index+1, lst[i], lst[val_index]
            if a==b:
                print -1
            else:
                print a,b