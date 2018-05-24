# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:48:10 2018

@author: jnguyen3
"""

def parent_tree(n):
    #set up initial dict
    #each key represents a node, the value is its parent
    output = {k:1001 for k in range(1,n+1)}
    return output

def tree(fpath):
    #goes through all edges, and picks one as its "parent"
    #if a parent already exist, take that as the new parent for the orphan
    #if both have parents, rewrite all instances 
    #of the other parent to match the new parent
    with open(fpath) as fhand:
        n = fhand.next()
        parent = parent_tree(int(n))
        #print parent
        for i in fhand:
            a,b = [int(x) for x in i.strip().split()]
            if parent[a] == 1001:
                if parent[b] == 1001:
                    parent[a] = a
                    parent[b] = a
                else:
                    parent[a] = parent[b]
            else:
                if parent[b] == 1001:
                    parent[b] = parent[a]
                else:
                    match = [k for k in parent if parent[k] == parent[b]]
                    for k in match:
                        parent[k] = parent[a]
        parents = set(val for val in parent.values() if val != 1001)                
        orphans = parent.values().count(1001)
        print parents
        print orphans
        return len(parents)-1 + orphans
        
fpath = r"C:\Users\jnguyen3\Downloads\rosalind_tree (2).txt"     

print tree(fpath)