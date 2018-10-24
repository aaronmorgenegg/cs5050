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

def addLists(A, B):
    n = len(A)
    C = [0]*n
    for i in range(n):
        C[i] = A[i]+B[i]
    return C

def subLists(lists):
    n = len(lists[0])
    C = [0]*n
    for i in range(n):
        value = 0
        for l in lists:
            value += l[i]
        C[i] = value
    return C

class PolynomialSolver:
    def schoolbook(self, P, Q):
        R = [0]*(len(P)+len(Q))
        for i in range(len(P)):
            for j in range(len(Q)):
                R[i+j] = P[i] * Q[j]
        return R

    def divide_conquer(self, P, Q):
        n = len(P)
        if(n <= 4):
            return self.schoolbook(P, Q)
        P1, P2 = splitList(P)
        Q1, Q2 = splitList(Q)
        A = self.divide_conquer(P1, Q1)
        D = self.divide_conquer(P2, Q2)
        E = self.divide_conquer(addLists(P1, P2), addLists(Q1, Q2))
        BC = subLists([E, A, D])
        # A + (B+C)x^n/2 + Dx^n
        result = A + D
        start = (len(result)-len(BC))//2
        end = len(BC) + start
        for i in range(start, end):
            try: result[i] += BC.pop(0)
            except Exception: return result
        return result

    def fft(self, P, Q):
        # TODO
        return self.schoolbook(P, Q)

    def computeOmegas(n):
        self.V = []
        for i in range(n):
            value = cmath.cos(2j*math.pi/n) + j*cmath.cos(2j*math.pi/n)
            self.V.append(value)
        
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
            if func_code == 3:
                self.computeOmegas(n)
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
        if func_code == 3:
            return self.fft

