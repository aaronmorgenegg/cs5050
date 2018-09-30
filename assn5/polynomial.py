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

class PolynomialSolver:
    def solvePolynomial(self, P, Q):
        R = [0]*(2*max(len(P), len(Q)))
        for i in range(len(P)):
            for j in range(len(Q)):
                R[i+j] = P[i] * Q[j]
        return R

    def getRandomPolynomial(self, n):
        polynomial = []
        for i in range(n):
            polynomial.append(random.uniform(MIN_COEFFICIENT, MAX_COEFFICIENT))
        return polynomial

    def runRandomTests(self, n, num_tests):
        results = [0]*num_tests
        for i in range(num_tests):
            results[i] = self.solvePolynomial(self.getRandomPolynomial(n), self.getRandomPolynomial(n))

    def runStudy(self, filename, n=32):
        while True:
            print("Running study with n = {}".format(n))
            time = TimeFunction(self.runRandomTests, n, NUM_TESTS_EACH_STEP)
            data = (n, time)
            self.saveData(data, filename)
            n *= 2

    def saveData(self, data, filename):
        with open(filename, "a") as myfile:
            myfile.write(str(data[0])+","+str(data[1])+"\n")

