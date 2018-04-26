# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:27:14 2018

@author: jnguyen3
"""


class Node():
    def __init__(self):
        self.neighbors = []
    def degrees(self):
        return len(self.neighbors)
    def addNeighbor(self,neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
            
        
if __name__ == "__main__":
    fname = r"C:\Users\jnguyen3\Downloads\rosalind_ddeg.txt"    
    with open(fname) as f:
        header = next(f)
        vertices = int(header.split()[0])
        node_list = { x : Node() for x in range(1,vertices+1)}
        for line in f:
            values = [int(x) for x in line.split()]
            node_list[values[0]].addNeighbor(values[1])
            node_list[values[1]].addNeighbor(values[0])
        adj_list = [node_list[x].neighbors for x in node_list]
        
        output = []        
        
        for x in range(1,vertices+1):
            total = 0
            for neighbor in node_list[x].neighbors:
                total += node_list[neighbor].degrees()
                #output.append(sum([node_list[neighbor].degrees() for neighbor in node_list[x].neighbors]))
                #for some reason, len of 0 is being output as 0.0
            output.append(total)
        print " ".join((str(x) for x in output))