# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:47:14 2018

@author: jnguyen3
"""

import math

def nCr(n,k):
    '''
    n choose k formula using factorials
    '''
    return math.factorial(n) / math.factorial(k) / math.factorial(n-k)
    
def main(n,k):
    total = 0
    while k <= n:
        #iterate through k until m
        total += nCr(n,k) % 1000000
        k+= 1
    return total % 1000000
    
print main(1707,608)