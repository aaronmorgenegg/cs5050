from algorithms import Backtrack, BoundingBacktrack, GreedyExpansionBacktrack
from tsp_reader import TSPReader

p01 = TSPReader.loadTSP("p01")

Backtrack(p01).invoke()
BoundingBacktrack(p01).invoke()
GreedyExpansionBacktrack(p01).invoke()
