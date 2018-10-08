#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# Naive polynomial solving algorithm,
# using method learned in school
########################

import random
import timeit

MIN_COEFFICIENT = -1
MAX_COEFFICIENT = 1
NUM_TESTS_EACH_STEP = 10

def TimeFunction(function, *args):
    """
    Function to time the runtime of another function
    Call with TimeFunction(function_name, arg1, arg2, ...,argn)
    """
    start_time = timeit.default_timer()
    function(*args)
    return timeit.default_timer() - start_time

def splitList(A):
    B = A[:len(A)//2]
    C = A[len(A)//2:]
    return B, C

class PolynomialSolver:
    def schoolbook(self, P, Q):
        R = [0]*(2*max(len(P), len(Q)))
        for i in range(len(P)):
            for j in range(len(Q)):
                R[i+j] = P[i] * Q[j]
        return R

    def divide_conquer(self, P, Q, result=None):
        if result is None: result = [0]*len(P)
        P1, P2 = splitList(P)
        Q1, Q2 = splitList(Q)
        A = divide_conquer(P1, Q1)
        D = divide_conquer(P2, Q2)
        P1P2 = [sum(x) for x in zip(P1, P2)]
        Q1Q2 = [sum(x) for x in zip(Q1, Q2)]
        E = divide_conquer(P1P2, Q1Q2)
        # A + (B+C)x^n/2 + Dx^n
        return A
        

    def getRandomPolynomial(self, n):
        polynomial = []
        for i in range(n):
            polynomial.append(random.uniform(MIN_COEFFICIENT, MAX_COEFFICIENT))
        return polynomial

    def runRandomTests(self, n, num_tests, func):
        results = [0]*num_tests
        for i in range(num_tests):
            results[i] = func(self.getRandomPolynomial(n), self.getRandomPolynomial(n))

    def runStudy(self, filename, func_code, n=32):
        algorithm = self._lookupFuncCode(func_code)
        while True:
            print("Running study with n = {}".format(n))
            time = TimeFunction(self.runRandomTests, n, NUM_TESTS_EACH_STEP, algorithm)
            data = (n, time)
            self.saveData(data, filename)
            n *= 2

    def saveData(self, data, filename):
        with open(filename, "a") as myfile:
            myfile.write(str(data[0])+","+str(data[1])+"\n")

    def _lookupFuncCode(self, func_code):
        if func_code == 1: 
            return self.schoolbook
        if func_code == 2:
            return self.divide_conquer

