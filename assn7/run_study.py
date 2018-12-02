from algorithms import Backtrack, BoundingBacktrack, GreedyExpansionBacktrack
from tsp_reader import TSPReader

import matplotlib.pyplot as plt

p01 = TSPReader.loadTSP("p01")

algorithms = [Backtrack, BoundingBacktrack, GreedyExpansionBacktrack]
problems = ["att48", "p01", "dantzig42", "fri26", "gr17"]


results = []
for problem in problems:
    result = []
    tsp = TSPReader.loadTSP(problem)
    for algorithm in algorithms:
        result.append(tsp.absolute_best_distance/algorithm(tsp).invoke())
    results.append(result)

plt.xticks([i for i in range(len(algorithms))], [i.__class__.__name__ for i in algorithms])
plt.yticks([i for i in range(len(problems))], problems)
plt.imshow(results, cmap="jet")
plt.colorbar()
plt.show()
