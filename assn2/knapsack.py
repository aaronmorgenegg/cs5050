#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# Knapsack algorithm with 2 knapsacks
########################

def KnapRecursive(n, k1, k2, s):
    """
    Recursive solution, where:
    n   == number of objects
    k1  == size of knapsack 1
    k2  == size of knapsack 2
    s   == sizes of objects
    """
    if k1 < 0 or k2 < 0: return False
    if k1 is 0 and k2 is 0: return True
    if n is 0: return False
    return (KnapRecursive(n-1, k1-s[n-1], k2, s) or 
            KnapRecursive(n-1, k1, k2-s[n-1], s) or 
            KnapRecursive(n-1, k1, k2, s)
            )

def KnapMemo():
    """
    Memoized solution, where:
    n   == number of objects
    k1  == size of knapsack 1
    k2  == size of knapsack 2
    s   == sizes of objects
    """
    pass

########################
# Tests
########################

k1 = 4
k2 = 6
s = [4,3,3]
n = len(s)
print("Running KnapRecursive(n={}, k1={}, k2={}, s={})".format(n,k1,k2,s))
print("Expected result: True")
print("Actual result: {}".format(KnapRecursive(n, k1, k2, s)))

