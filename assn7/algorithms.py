from constants import TIME_LIMIT, VERBOSITY
from timer import Timer


class Algorithm:
    def __init__(self, TSP, time_constraint=TIME_LIMIT):
        self.TSP = TSP
        self.time_constraint = time_constraint
        self.best_so_far = 1000000
        self.start_time = Timer.getCurrentTime()

    def invoke(self):
        self._recurse([0], [i for i in range(1, len(self.TSP.distances))])
        if VERBOSITY > 1: print("{} algorithm found a solution of length {} in {} seconds, compared to the best possible solution of {}".format(self.__class__.__name__, self.best_so_far, self.time_constraint, self.TSP.absolute_best_distance))
        return self.best_so_far

    def outOfTime(self):
        if Timer.getCurrentTime()-self.start_time > self.time_constraint:
            return True
        return False

    def _recurse(self, tour, remaining_cities):
        print("Not Implemented")

class Backtrack(Algorithm):
    def _recurse(self, tour, remaining_cities):
        if self.outOfTime(): return
        if len(remaining_cities) == 0:
            self.best_so_far = min(self.best_so_far, self.TSP.computeDistance(tour))
        else:
            for city in remaining_cities:
                self._recurse(tour+[city], [x for x in remaining_cities if x != city])


class BoundingBacktrack(Algorithm):
    def _recurse(self, tour, remaining_cities):
        if self.outOfTime(): return
        if len(remaining_cities) == 0:
            self.best_so_far = min(self.best_so_far, self.TSP.computeDistance(tour))
        else:
            if self.TSP.computeDistance(tour) > self.best_so_far: return # Bounding against best solution so far
            for city in remaining_cities:
                self._recurse(tour+[city], [x for x in remaining_cities if x != city])

def boundingBacktrack(TSP, time_constraint=TIME_LIMIT):
    start_time = Timer.getCurrentTime()
    while Timer.getCurrentTime()-start_time < TIME_LIMIT:
        pass


def greedyExpansionBacktrack(TSP, time_constraint=TIME_LIMIT):
    start_time = Timer.getCurrentTime()
    while Timer.getCurrentTime()-start_time < TIME_LIMIT:
        pass


def hillClimbSwap(TSP, time_constraint=TIME_LIMIT):
    start_time = Timer.getCurrentTime()
    while Timer.getCurrentTime()-start_time < TIME_LIMIT:
        pass


def hillClimbReverse(TSP, time_constraint=TIME_LIMIT):
    start_time = Timer.getCurrentTime()
    while Timer.getCurrentTime()-start_time < TIME_LIMIT:
        pass
