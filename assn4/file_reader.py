#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# File reader to read in dna files
########################

import re

def readFile(filename):
    with open(filename, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    data = re.sub('[^acgtACGT]', '', data)
    return data.upper()

