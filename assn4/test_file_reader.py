#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# test cases for file reader
# run 'python test_file_reader.py'
########################

from file_reader import *

def runTest(filename):
    print("Opening file:{}".format(filename))
    data = readFile(filename)
    print("File contents:{}\n".format(data))

runTest("dna_samples/prototypical_human_01.txt")

