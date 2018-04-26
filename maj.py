# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:17:01 2018

@author: jnguyen3
"""

if __name__== "__main__":
    fname = r"C:\Users\jnguyen3\Downloads\rosalind_maj (1).txt"
    #moore voting
    with open(fname) as f:
        header = next(f).split()
        lines = int(header[0])
        length = int(header[1])
        limit = int(length/2)
        output = []
        for line in f:
            m = None
            counter = 0
            lst = line.split()
            for item in lst:
                if m == None or counter == 0:
                    m = item
                    continue
                if m == item:
                    counter += 1
                else:
                    counter -= 1
            if lst.count(m) > limit:
                output.append(m)
            else:
                output.append("-1")
    print " ".join(output)
    
    if False:
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
    