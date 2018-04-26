# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 14:20:25 2018

@author: jnguyen3
"""

if __name__ == "__main__":
    fname = r"C:\Users\jnguyen3\Downloads\rosalind_mer (1).txt"
    with open(fname) as f:
        f.next()
        A = [int(x) for x in f.next().split()]
        f.next()
        B = [int(x) for x in f.next().split()]
        C = []
        print A, B
        while len(A) + len(B) > 0:
            if len(A) == 0:
                C += B
                break
            if len(B) == 0:
                C += A
                break
            if A[0] < B[0]:
                C.append(A.pop(0))
            else:
                C.append(B.pop(0))
        output = " ".join(str(x) for x in C)
        print output
    '''
    with open("output.txt", "w") as f:
        f.write(output)
    '''