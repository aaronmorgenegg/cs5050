from algorithms import Backtrack, BoundingBacktrack
from tsp_reader import TSPReader

p01 = TSPReader.loadTSP("p01")

Backtrack(p01).invoke()
BoundingBacktrack(p01).invoke()
