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
    print("Running test with\n  A: {}\n  B: {}".format(A, B))
    difference = test.matchDP()
    print("Difference Score: {}".format(difference))
    alignment = test.traceback()
    print("  Alignment A: {}\n  Alignment B: {}\n".format(alignment[0],alignment[1]))
    test.printAlignmentToFile("test_dna.log")

runTest("GCC","GCC")

runTest("ATGC","ATGG")

runTest("ATATATA", "TATATAT")

runTest("GATTACA", "GCATGCT")

runTest("GCTA","GCTAATTACC")

runTest("GCTAATTACC","GCTA")

runTest(getRandomString(95+random.randint(0, 10)),
        getRandomString(95+random.randint(0, 10)))

