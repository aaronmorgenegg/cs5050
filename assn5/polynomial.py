#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# Naive polynomial solving algorithm,
# using method learned in school
########################

import random

MIN_COEFFICIENT = -1
MAX_COEFFICIENT = 1

class PolynomialSolver:
    def solvePolynomial():
        pass

    def getRandomPolynomial(n):
        polynomial = []
        for i in range(n):
            polynomial.append(random.uniform(MIN_COEFFICIENT, MAX_COEFFICIENT))
        return polynomial

