from algorithms import Backtrack, BoundingBacktrack, GreedyExpansionBacktrack, HillClimbSwap, HillClimbReverse
from tsp_reader import TSPReader

import matplotlib.pyplot as plt

p01 = TSPReader.loadTSP("p01")

algorithms = [Backtrack, BoundingBacktrack, GreedyExpansionBacktrack, HillClimbSwap, HillClimbReverse]
problems = ["att48", "p01", "dantzig42", "fri26", "gr17"]
graph_name = "results"


results = []
for problem in problems:
    result = []
    tsp = TSPReader.loadTSP(problem)
    for algorithm in algorithms:
        result.append(tsp.absolute_best_distance/algorithm(tsp).invoke())
    results.append(result)

plt.yticks([i for i in range(len(algorithms))], [i.__name__ for i in algorithms])
plt.xticks([i for i in range(len(problems))], problems)
plt.ylabel("Algorithm")
plt.xlabel("Problem Set")
plt.title("Travelling Salesman Algorithm Accuracy")
plt.imshow(list(map(list, zip(*results))), cmap="jet")
plt.colorbar()
plt.tight_layout()
plt.savefig("{}.png".format(graph_name))
plt.show()
