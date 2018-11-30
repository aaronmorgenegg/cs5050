from constants import TIME_LIMIT
from timer import Timer


def backtrack(TSP, time_constraint=TIME_LIMIT):
    start_time = Timer.getCurrentTime()
    remaining_cities = [i for i in range(len(TSP.distances))]
    while Timer.getCurrentTime()-start_time < TIME_LIMIT:
        pass


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
