#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# File reader to read in dna files
########################

def readFile(filename):
    with open(filename, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    data = data.translate({ord(c): None for c in '1234567890    '})
    return data.upper()

