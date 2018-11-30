from constants import DISTANCE_FILE_ROOT, SOLUTION_DISTANCE_FILE_ROOT
from tsp import TSP


class TSPReader:
    @staticmethod
    def loadTSP(name):
        """Returns a TSP problem instance from a study name"""
        with open(DISTANCE_FILE_ROOT.format(name), "r") as myfile:
            lines = myfile.readlines()
        distances = []
        for line in lines:
            distance = line.split()
            distance = [int(d.strip()) for d in distance]
            distances.append(distance)
        with open(SOLUTION_DISTANCE_FILE_ROOT.format(name), "r") as myfile:
            line = myfile.readline()
        absolute_best_distance = int(line.strip())

        return TSP(name, distances, absolute_best_distance)
