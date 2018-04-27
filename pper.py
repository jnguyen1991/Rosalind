# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:33:01 2018

@author: jnguyen3
"""

import math

def pper(n,k):
    #built in math.factorial
    result = math.factorial(n)/math.factorial(n-k) % 1000000
    return result
    
def pper_mod(n,k):
    #uses loop, mod at each step
    result = 1
    for i in range(k):
        result *= n-i
        result %= 1000000
    return result
    
if __name__ == "__main__":
    print pper_mod(97,9)