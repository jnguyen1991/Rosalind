# -*- coding: utf-8 -*-
"""
IN PROGRESS
"""

def lia(k, N):
    table = {"AABB":1/float(16),
             "AABb":2/float(16),
             "AAbb":1/float(16),
             "AaBB":2/float(16),
             "AaBb":4/float(16),
             "Aabb":2/float(16),
             "aaBB":1/float(16),
             "aaBb":2/float(16),
             "aabb":1/float(16)
             }
    AaBb_table = {"AABB":1/(9,
             "AABb":,
             "AAbb":,
             "AaBB":,
             "AaBb":4/float(16),
             "Aabb":2/float(16),
             "aaBB":1/float(16),
             "aaBb":2/float(16),
             "aabb":1/float(16)
             }
    init = table
    first = {key:v * table[key] for key,v in init.items()}
    second = {key:v * table[key] for key,v in first.items()}
    print first
    print second

if __name__ == "__main__":
    lia(2,1)