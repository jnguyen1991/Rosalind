# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:33:04 2017

@author: jnguyen3
"""

import sys

def main():
    if len(sys.argv) == 2:
        fname= sys.argv[1]
    else:
        print("Wrong number of args, expected 1, received: " + str(len(sys.argv) - 1))
        fname = input("Enter file path: ")
    n = []
    m = []
    output = []   
    with open(fname, 'r') as fhand:
        #2 lines of header for the input file
        #don't need them, because we find out length with len function
        fhand.readline()
        fhand.readline()
        #n is the array to search
        n = fhand.readline().strip().split(" ")
        #m is the elements to find
        m = fhand.readline().strip().split(" ")
        #changing from string to int type 
        n = [int(i) for i in n]
        m = [int(i) for i in m]
    for i in m:
        #make a list with str results
        output.append(str(recursive_binary_search(i, n, 0, len(n)-1)))
        
    with open(fname + "_output.txt", 'w') as fout:
        #convert python list to string
        fout.write(" ".join(output))

def recursive_binary_search(i, n, start, end):
    '''
    i represents element to find
    n represents list of elements to check for
    start is the beginning of search area, should be 0 for first call
    end is the end of search area, should be len(n)-1 for first call
    '''
    #could not find, end of search
    if end < start:
        return -1
    #check the middle element
    mid = (end + start) / 2
    if i == n[mid]:
        #indexing for results starts at 1
        #so add 1 to match output, to start at 0
        #remove the + 1
        return mid + 1
    else:
        #search item is higher value than middle, check top half
        if i > n[mid]:
            return recursive_binary_search(i, n, mid+1, end)
        #search item is lower value, check bottom half
        else:
            return recursive_binary_search(i, n, start, mid-1) 
            
if __name__ == "__main__":
    main()
