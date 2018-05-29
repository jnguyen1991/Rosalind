# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:48:11 2018

@author: jnguyen3
"""

def sset(n, output):
    for i in n:
        temp = n.copy()
        temp.remove(i)
        if temp not in output:
            output.append(temp)
            output.append(sset(temp, output))

def main(n):
    '''
    Recursive solution, doesn't work well for large numbers
    '''
    largest = set(range(1,n+1))
    output = []
    output.append(largest)
    output.append(sset(largest, output))
    return len([x for x in output if x != None])
    #print sset(lst)

x = 827   
    
#print main(x)
    
print 2**x % 1000000

#or pow(2,x,1000000) for better efficiency