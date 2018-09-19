#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# String matching algorithm used 
# to match DNA sequences
########################

DEBUG = True

class DNAMatcher:
    def __init__(self, A, B, S=None, D=None):
        self.A = A # String A
        self.B = B # String B
        self.cache = self.initCache() # Cache for DP
        self.S = self.initSimilarityMatrix(S) # Similarity Matrix
        self.D = self.initGapPenalty(D) # Gap Penalty

    def initCache(self):
        cache = []
        for i in range(len(self.B)):
            cache.append([])
        return cache

    def initSimilarityMatrix(self, S):
        if S is None:
            return [[10, -1, -3, -4],
                    [-1, 7, -5, -3],
                    [-3, -5, 9, 0],
                    [-4, -3, 0, 8]]
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
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                match = matchDP(i-1, j-1) + self.S(A[i], self.B[j])
                delete = matchDP(i-1, j) + d
                insert = matchDP(i, j-1) + d
                self.cache[i][j] = max(match, delete, insert)

