# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:08:25 2017

@author: jnguyen3
"""

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_memo(n, table):
    if len(table) == 0:
        table = {0:0,1:1}
    if n in table:
        return table[n]
    else:
        table[n] = fib_memo(n-1, table) + fib_memo(n-2, table)
        return table[n]

if __name__ == '__main__':
    table = {}
    #print(fib(100))
    n = 40
    print(fib_memo(n, table))
    #print(fib(n))