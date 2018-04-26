# -*- coding: utf-8 -*-
"""
IN PROGRESS
"""

from Bio import SeqIO
import sys
file_input = r"test"

def long(fname):
    records = list(SeqIO.parse(fname,"fasta"))
    limit = len(records)
    output = records[0].seq
    records = records[1:]
    i = 0
    counter = 1
    while len(records) > 0:

        try:
            current_seq = records[i]
        except Exception as e:
            print(e)
            print(i)
            print(current_seq.id)
            print("breaking")
            sys.exit()
        
        half = len(current_seq.seq)//2
        if current_seq.seq[:half] in output:
            match = current_seq.seq[:half]
            loc = output.find(match)
            output = output[loc:] + current_seq.seq
            records.pop(i)
            i = 0
            counter = 0
        elif current_seq.seq[half:] in output:
            match = current_seq.seq[half:]
            loc = output.find(match)
            output = current_seq.seq + output[loc+half+1:]
            records.pop(i)
            i = 0
            counter = 0
        else:
            i += 1
            if i == len(records):
                counter += 1
                i = counter
    print(output)
    print(limit)
    print(len(records))
    return

if __name__ == "__main__":
    long(file_input)