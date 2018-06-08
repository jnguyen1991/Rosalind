# -*- coding: utf-8 -*-
"""
Created on Fri Jun 08 13:42:49 2018

@author: jnguyen3
"""

import numpy as np

def lgis(n, inc=True):
    '''
    n is a list of int
    '''
    size = len(n)
    lst = []
    for i in n:
        if len(lst) == 0:
            lst.append([i])
            continue
        ends = [x[-1] for x in lst]
        if inc:
            if i < min(ends):
                lst[0] = [i]
                continue
            if i > max(ends):
                lst.append(lst[-1]+[i])
                continue
            for j in range(len(ends)-1,-1,-1):    
                if ends[j] > i and ends[j-1] < i:
                    lst[j] = lst[j][:-1] + [i]
                    break
        else:
            if i > max(ends):
                lst[0] = [i]
                continue
            if i < min(ends):
                lst.append(lst[-1]+[i])
                continue
            for j in range(len(ends)-1,-1,-1):
                if ends[j] < i and ends[j-1] > i:
                    lst[j] = lst[j][:-1] + [i]
                    break
        
    return lst[-1]
            


def readFiles(fin):
    with open(fin) as fhand:
        fhand.next()
        output = fhand.next()
        output = [int(x) for x in output.split()]
        return output

finput = r"C:\Users\jnguyen3\Downloads\rosalind_lgis (1).txt"
output = readFiles(finput)
#print output

output = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
a=lgis(output, inc=True)    
print " ".join([str(x) for x in a])
b=lgis(output, inc=False)
print " ".join([str(x) for x in b])