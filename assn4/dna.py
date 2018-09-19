#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# String matching algorithm used 
# to match DNA sequences
########################

import random

DEBUG = False

def getRandomString(n):
    string = ''
    for i in range(n):
        string += random.choice('AGCT')
    return string

class DNAMatcher:
    def __init__(self, A, B, S=None, D=None):
        self.A = A # String A
        self.B = B # String B
        if DEBUG: print("A: {}".format(self.A))
        if DEBUG: print("B: {}".format(self.B))
        self.cache = self.initCache() # Cache for DP
        if DEBUG: print("Cache: {}".format(self.cache))
        self.S = self.initSimilarityMatrix(S) # Similarity Matrix
        if DEBUG: print("S: {}".format(self.S))
        self.D = self.initGapPenalty(D) # Gap Penalty
        if DEBUG: print("D: {}".format(self.D))

    def initCache(self):
        cache = []
        for i in range(len(self.A)):
            cache.append([None]*len(self.B))
        return cache

    def initSimilarityMatrix(self, S):
        if S is None:
            return {'AA': 10, 'AG': -1, 'AC': -3, 'AT': -4,
                    'GA': -1, 'GG': 7, 'GC': -5, 'GT': -3,
                    'CA': -3, 'CG': -5, 'CC': 9, 'CT': 0,
                    'TA': -4,'TG': -3, 'TC': 0, 'TT': 9}
        return S

    def initGapPenalty(self, D):
        if D is None:
            return -5
        return D

    def matchDP(self):
        for i in range(len(self.A)):
            self.cache[i][0] = self.D*i
        for j in range(len(self.B)):
            self.cache[0][j] = self.D*j
        for i in range(1, len(self.A)):
            for j in range(1, len(self.B)):
                match = self.cache[i-1][j-1] + self.S[self.A[i]+self.B[j]]
                delete = self.cache[i-1][j] + self.D
                insert = self.cache[i][j-1] + self.D
                self.cache[i][j] = max(match, delete, insert)
        return self.cache[len(self.A)-1][len(self.B)-1]

    def alignment(self):
        alignmentA = ""
        alignmentB = ""
        i = len(self.A)
        j = len(self.B)
        while i > 0 or j > 0:
            if i > 0 and j > 0 and self.cache[i][j] == self.cache[i-1][j-1]+self.S[self.A[i]+self.[B[i]]:
                alignmentA += self.A[i]
                alignmentB += self.B[i]
                i -= 1
                j -= 1
            else if i > 0 and self.cache[i][j] == self.cache[i-1][j] + self.D:
                alignmentA += self.A[i]
                alignmentB += "_"
                i -= 1
            else:
                alignmentA += "_"
                alignmentB += self.B[i]
                j -= 1
        print(alignmentA)
        print(alignmentB)

