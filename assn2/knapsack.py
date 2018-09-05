#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# Knapsack algorithms with 2 knapsacks, with 
# both recursive and memoized algorithms
########################

RUN_SIMPLE_TESTS = True        # Toggle running simple, hardcoded tests
RUN_SIMPLE_RANDOM_TESTS = True # Toggle running simple, random tests
RUN_TIMED_TESTS = True         # Toggle running repeated, timed, random tests

import random
import timeit

# Dictionary for memoizing data, indexed with a tuple (n, k1, k2)
cacheValid = {}

# Helper dictionary to hold runtime data to be averaged.
timeData = {}

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
    return (KnapRecursive(n-1, k1-s[n-1], k2, s) or # Put it in knapsack 1
            KnapRecursive(n-1, k1, k2-s[n-1], s) or # Put it in knapsack 2
            KnapRecursive(n-1, k1, k2, s) # Don't put it in either knapsack
            )

def KnapMemo(n, k1, k2, s):
    """
    Memoized solution, where:
    n   == number of objects
    k1  == size of knapsack 1
    k2  == size of knapsack 2
    s   == sizes of objects
    """
    try: # Try returning the memoized value, if it exists
        return cacheValid[(n, k1, k2)]
    except KeyError:
        pass
    if k1 < 0 or k2 < 0: 
        cacheValid[(n, k1, k2)] = False # Make sure to memoize the results
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
# Test Functions
########################

def TestKnapRecursive(n, k1, k2, s, e):
    """Helper function to test KnapRecursive function and print info"""
    print("\nRunning KnapRecursive(n={}, k1={}, k2={}, s={})".format(n,k1,k2,s))
    print("Expected result: {}".format(e))
    result = KnapRecursive(n, k1, k2, s)
    print("Actual result: {}\n".format(result))
    return result

def TestKnapMemo(n, k1, k2, s, e):
    print("\nRunning KnapMemo(n={}, k1={}, k2={}, s={})".format(n,k1,k2,s))
    print("Expected result: {}".format(e))
    result = KnapMemo(n, k1, k2, s)
    print("Actual result: {}\n".format(result))
    return result

def TestBothWithRandomData(repetitions):
    """Compare results of both algorithms with random data, repeated of course"""
    for test in range(repetitions):
        print("\nRunning random test number {}\n".format(test))
        k1 = random.randint(0, 20)
        k2 = random.randint(0, 20)
        n = random.randint(0, 20)
        s = []
        for i in range(n):
            s.append(random.randint(0,20))
        print("Running TestBothWithRandomData(n={}, k1={}, k2={}, s={})".format(n,k1,k2,s)) 
        kr = KnapRecursive(n, k1, k2, s)
        km = KnapMemo(n, k1, k2, s)
        if kr != km: print("ERROR: Recursive and Memoized solutions differ.")
        print("KnapRecursive={}\nKnapMemo={}\n".format(kr,km))

def GetRandomSizes(n, m):
    s = []
    for i in range(n):
        s.append(random.randint(0, m))
    return s

def ProblemGenerator(k1, k2, nmin, nmax, nstep, m, function, use_time_data, reps):
    """Generates random data for n and s,
    runs the given algorithm multiple times,
    increasing n from nmin to nmax.
    Prints the runtime for each value of n."""
    for test in range(reps):
        for n in range(nmin, nmax, nstep):
            s = GetRandomSizes(n, m)
            print("n:{}".format(n))
            time_result = TimeFunction(function, n, k1, k2, s)
            print("Runtime: {}".format(time_result))
            if use_time_data: 
                try:
                    timeData[n].append(time_result)
                except KeyError:
                    timeData[n] = [time_result]

def TimeFunction(function, *args):
    """
    Function to time the runtime of another function
    Call with TimeFunction(function_name, arg1, arg2, ...,argn)
    """
    start_time = timeit.default_timer()
    function(*args)
    return timeit.default_timer() - start_time

########################
# Test Cases
########################

if RUN_SIMPLE_TESTS:
    print("------------------------------------------")
    print("Running simple tests of KnapRecursive and KnapMemo")
    print("------------------------------------------")
    
    TestKnapRecursive(3, 4, 6, [4,3,3], "True")
    TestKnapRecursive(4, 4, 6, [4,3,2,2], "False")
    
    TestKnapMemo(3, 4, 6, [4,3,3], "True")
    TestKnapMemo(4, 4, 6, [4,3,2,2], "False")
    
    print("------------------------------------------")
    print("Done running simple tests of KnapRecursive and KnapMemo")
    print("------------------------------------------")

if RUN_SIMPLE_RANDOM_TESTS:
    print("------------------------------------------")
    print("Running randomly generated tests comparing KnapRecursive and KnapMemo")
    print("------------------------------------------")
    
    TestBothWithRandomData(5)
    
    print("------------------------------------------")
    print("Done running randomly generated tests comparing KnapRecursive and KnapMemo")
    print("------------------------------------------")

if RUN_TIMED_TESTS:
    print("------------------------------------------")
    print("Running timed tests with randomly generated data.")
    
    k1 = 100
    k2 = 100
    nmin = 10
    nmax = 200
    nstep = 10
    m = 25
    function = KnapRecursive
    use_time_data = True
    reps = 3
    
    ProblemGenerator(k1, k2, nmin, nmax, nstep, m, function, use_time_data, reps)
    
    print(timeData)

