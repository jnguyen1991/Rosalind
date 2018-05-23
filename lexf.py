# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:50:54 2018

@author: jnguyen3
"""

alphabet = "A B C D E"
n=4

alpha = alphabet.split()

def lexf(output, alpha):
    new_output = []
    for i in output:
        for j in alpha:
            new_output.append(i + j)
    return new_output
            
output = alpha
while n > 1:
    output = lexf(output,alpha)
    n-= 1

for i in output:
    print i