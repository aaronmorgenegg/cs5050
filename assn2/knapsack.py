#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# Knapsack algorithm with 2 knapsacks
########################

cacheValid = {}

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

def KnapMemo(n, k1, k2, s):
    """
    Memoized solution, where:
    n   == number of objects
    k1  == size of knapsack 1
    k2  == size of knapsack 2
    s   == sizes of objects
    """
    try:
        return cacheValid[(n, k1, k2)]
    except KeyError:
        pass
    if k1 < 0 or k2 < 0: 
        cacheValid[(n, k1, k2)] = False
        return cacheValid[(n, k1, k2)]
    if k1 is 0 and k2 is 0: 
        cacheValid[(n, k1, k2)] = True
        return cacheValid[(n, k1, k2)]
    if n is 0: 
        cacheValid[(n, k1, k2)] = False
        return cacheValid[(n, k1, k2)]
    return (KnapRecursive(n-1, k1-s[n-1], k2, s) or
            KnapRecursive(n-1, k1, k2-s[n-1], s) or
            KnapRecursive(n-1, k1, k2, s)
            )

########################
# Tests
########################

def TestKnapRecursive(k1, k2, s, e):
    n = len(s)
    print("\nRunning KnapRecursive(n={}, k1={}, k2={}, s={})".format(n,k1,k2,s))
    print("Expected result: {}".format(e))
    print("Actual result: {}\n".format(KnapRecursive(n, k1, k2, s)))

def TestKnapMemo(k1, k2, s, e):
    n = len(s)
    print("\nRunning KnapMemo(n={}, k1={}, k2={}, s={})".format(n,k1,k2,s))
    print("Expected result: {}".format(e))
    print("Actual result: {}\n".format(KnapMemo(n, k1, k2, s)))


print("Running simple tests of KnapRecursive and KnapMemo")

TestKnapRecursive(4, 6, [4,3,3], "True")
TestKnapRecursive(4, 6, [4,3,2,2], "False")

TestKnapMemo(4, 6, [4,3,3], "True")
TestKnapMemo(4, 6, [4,3,2,2], "False")

print("Done running simple tests of KnapRecursive and KnapMemo")

print("Running randomly generated tests comparing KnapRecursive and KnapMemo")


print("Done running randomly generated tests comparing KnapRecursive and KnapMemo")


