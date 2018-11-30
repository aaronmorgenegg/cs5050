from constants import DISTANCE_FILE_ROOT


class TSPReader:
    @staticmethod
    def buildFromDistanceFile(name):
        """Returns a TSP problem instance from a given distance file"""
        with open(DISTANCE_FILE_ROOT.format(name), "r") as myfile:
            lines = myfile.readlines()
        distances = []
        for line in lines:
            distance = line.split()
            distance = [int(d.strip()) for d in distance]

            distances.append(distance)
        print(distances)
