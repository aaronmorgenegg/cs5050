import random

from constants import TIME_LIMIT, VERBOSITY, STUCK_COUNT
from timer import Timer


class Algorithm:
    def __init__(self, TSP, time_constraint=TIME_LIMIT):
        self.TSP = TSP
        self.time_constraint = time_constraint
        self.best_so_far = 1000000
        self.start_time = Timer.getCurrentTime()

    def invoke(self):
        self._recurse([0], [i for i in range(1, len(self.TSP.distances))])
        if VERBOSITY > 1: print("{}: {} algorithm found a solution of length {} in {} seconds, compared to the best possible solution of {}".format(self.TSP.name, self.__class__.__name__, self.best_so_far, self.time_constraint, self.TSP.absolute_best_distance))
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


class GreedyExpansionBacktrack(Algorithm):
    def _recurse(self, tour, remaining_cities):
        if self.outOfTime(): return
        if len(remaining_cities) == 0:
            self.best_so_far = min(self.best_so_far, self.TSP.computeDistance(tour))
        else:
            if self.TSP.computeDistance(tour) > self.best_so_far: return # Bounding against best solution so far
            # Greedy expansion - recursively explore routes to closer cities first
            sorted_remaining_cities = self._sortClosestCities(tour[-1], remaining_cities)
            for city in sorted_remaining_cities:
                self._recurse(tour+[city], [x for x in sorted_remaining_cities if x != city])

    def _sortClosestCities(self, city, remaining_cities):
        return sorted(remaining_cities, key=lambda x: self.TSP.distances[city][x])


class HillClimbSwap(Algorithm):
    def _recurse(self, tour, remaining_cities):
        solution = random.shuffle([remaining_cities] + [tour])
        distance = self.TSP.computeDistance(solution)
        if distance < self.best_so_far: self.best_so_far = distance
        stuck_counter = STUCK_COUNT
        while stuck_counter > 0:
            if self.outOfTime(): return
            indexes = random.sample(range(0, len(solution)), 2) # gives list of 2 indexes to swap
            new_solution = self._mutate(solution, indexes)
            new_distance = self.TSP.computeDistance(new_solution)
            if new_distance <= distance:
                solution = new_solution
                stuck_counter = STUCK_COUNT
                if new_distance <= self.best_so_far:
                    self.best_so_far = new_distance
            stuck_counter -= 1
        self._recurse(tour, remaining_cities)

    def _mutate(self, tour, indexes):
        new_tour = list(tour)
        new_tour[indexes[0]], new_tour[indexes[1]] = new_tour[indexes[1]], new_tour[indexes[0]]
        return new_tour


class HillClimbReverse(HillClimbSwap):
    # Same as HillClimbSwap but uses a different mutation process
    def _mutate(self, tour, indexes):
        indexes.sort()
        new_tour = list(tour)
        new_tour[indexes[0]:indexes[1]] = new_tour[indexes[0]:indexes[1]][::-1]
        return new_tour
