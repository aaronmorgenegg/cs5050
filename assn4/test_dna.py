#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# test cases for string matching
# dna algorithms
# run 'python test_dna.py'
########################

from dna import *

def runTest(A, B, S=None, D=None):
    test = DNAMatcher(A, B, S=S, D=D)
    print("Running test with\n A: {}\n B: {}\n".format(A, B))
    difference = test.matchDP()
    print("Difference Score: {}".format(difference))
    alignment = test.traceback()
    print("Alignment: {}".format(alignment))

runTest(getRandomString(95+random.randint(0, 10)),
        getRandomString(95+random.randint(0, 10)))

