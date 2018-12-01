

class TSP:
    def __init__(self, name, distances, absolute_best_distance):
        self.name = name
        self.distances = distances
        self.absolute_best_distance = absolute_best_distance

    def computeDistance(self, tour):
        distance = 0
        for i in range(len(tour)):
            try:
                distance += self.distances[i][i-1]
            except IndexError:
                pass
        return distance
