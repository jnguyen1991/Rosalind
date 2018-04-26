# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:57:09 2018

@author: jnguyen3
"""

class Deg():
    def __init__(self, header):
        self.degrees = {}
        header = header.split()
        self.vertices = int(header[0])
        self.edges = int(header[1])
    
    def add_point(self, line):
        line = line.split()
        first_key = int(line[0])
        second_key = int(line[1])
        if first_key in self.degrees:
            self.degrees[first_key] += 1
        else:
            self.degrees[first_key] = 1
        
        if second_key in self.degrees:
            self.degrees[second_key] += 1
        else:
            self.degrees[second_key] = 1
            
    
    def print_degrees(self):
        output = []
        for i in range(1,self.vertices+1):
            if i in self.degrees:
                output.append(str(self.degrees[i]))
            else:
                output.append("0")
        print " ".join(output)

if __name__ == "__main__":
    fname = r"C:\Users\jnguyen3\Downloads\rosalind_deg (2).txt"    
    with open(fname) as f:
        header = next(f)
        deg = Deg(header)
        for line in f:
            deg.add_point(line)
        deg.print_degrees()