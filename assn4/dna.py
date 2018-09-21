#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# String matching algorithm used 
# to match DNA sequences
########################

import random

DEBUG = False
REVERSE_ALIGNMENT = False

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
        self.S = self.initSimilarityMatrix(S) # Similarity Matrix
        self.D = self.initGapPenalty(D) # Gap Penalty

    def initCache(self):
        cache = []
        for i in range(len(self.A)):
            cache.append([None]*len(self.B))
        return cache

    def initSimilarityMatrix(self, S):
        if S is None:
            return {'AA': 5, 'AG': -2, 'AC': -1, 'AT': -1,
                    'GA': -2, 'GG': 5, 'GC': -3, 'GT': -2,
                    'CA': -1, 'CG': -3, 'CC': 5, 'CT': -2,
                    'TA': -1,'TG': -2, 'TC': -2, 'TT': 5}
        return S

    def initGapPenalty(self, D):
        if D is None:
            return -3
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

    def traceback(self):
        alignmentA = ""
        alignmentB = ""
        i = len(self.A)-1
        j = len(self.B)-1
        while i > 0 or j > 0:
            if i > 0 and j > 0 and self.cache[i][j] == self.cache[i-1][j-1]+self.S[self.A[i]+self.B[j]]:
                if REVERSE_ALIGNMENT:
                    alignmentA = "{}{}".format(alignmentA,self.A[i])
                    alignmentB = "{}{}".format(alignmentB,self.B[j])
                else:
                    alignmentA = "{}{}".format(self.A[i],alignmentA)
                    alignmentB = "{}{}".format(self.B[j],alignmentB)
                i -= 1
                j -= 1
            elif i > 0 and self.cache[i][j] == self.cache[i-1][j] + self.D:
                if REVERSE_ALIGNMENT:
                    alignmentA = "{}{}".format(alignmentA,self.A[i])
                    alignmentB = "{}{}".format(alignmentB,"_")
                else:
                    alignmentA = "{}{}".format(self.A[i],alignmentA)
                    alignmentB = "{}{}".format("_",alignmentB)
                i -= 1
            else:
                if REVERSE_ALIGNMENT:
                    alignmentA = "{}{}".format(alignmentA,"_")
                    alignmentB = "{}{}".format(alignmentB,self.B[j])
                else:
                    alignmentA = "{}{}".format("_",alignmentA)
                    alignmentB = "{}{}".format(self.B[j],alignmentB)
                j -= 1
        return (alignmentA, alignmentB)

