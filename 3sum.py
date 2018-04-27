# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 15:45:46 2018

@author: jnguyen3
"""

def brute(line):
    lst = [int(x) for x in line.split()]
    for a in range(len(lst)-2):
        for b in range(a+1,len(lst)-1):
            for c in range(b+1,len(lst)):
                print "FALSE",a,b,c
                if lst[a]+lst[b]+lst[c] == 0:
                    print a+1,b+1,c+1
                    output = " ".join([str(x) for x in [a+1,b+1,c+1]])
                    return output
    return -1
    
def threesum(line):
    lst = [int(x) for x in line.split()]
    dct = {key:val for key,val in enumerate(lst)}
    sort = sorted(dct, key=dct.get)
    for i in range(len(sort)-2):
        j = i+1
        k = len(sort)-1
        while j < k:
            #print lst[sort[i]],lst[sort[j]],lst[sort[k]]
            total = lst[sort[i]] + lst[sort[j]] + lst[sort[k]]
            #print total
            if total == 0:
                output = " ".join([str(x) for x in sorted([sort[i]+1, sort[j]+1, sort[k]+1])])
                return output
            if total > 0:
                k -= 1
            else:
                j += 1
    return "-1"    

if __name__ == "__main__":
    fname = r"C:\Users\jnguyen3\Downloads\rosalind_3sum (1).txt"
    #brute force O(n^3)    
    with open(fname) as fhand:
        length = int(fhand.next().split()[1])
        for line in fhand:
            print threesum(line)
                
            '''
            for i in range(length-2):
                for j in range(i+1, length-1):
                    val = lst[i]+lst[j]
                    print i,j, val
                    if -val in lst[j+1:]:
                        print val,-val
            '''