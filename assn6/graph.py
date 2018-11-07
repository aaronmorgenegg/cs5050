import matplotlib.pyplot as graph
import numpy as np
import matplotlib.patches as mpatches
from scipy.optimize import curve_fit
from constants import *

SHOW_GRAPHS = True

def polyFunc(x, a, b, c):
    return a * np.exp(b*x)+c

def fitCurve(data, color):
    graph.plot(data[0], data[1], color, label="Fitted Curve")
    graph.xscale("log")
    graph.yscale("log")
    graph.xlabel("Problem Size (n)")
    graph.ylabel("Average Runtime (s)")
    graph.title("Performance of Algorithms")
    graph.grid(True)

def readData(filename):
    with open(filename, "r") as myfile:
        data = myfile.readlines()
    time_data = []
    n_data = []
    for i in range(len(data)):
        s = data[i].split(",")
        n = int(s[0])
        time = float(s[1])
        n_data.append(n)
        time_data.append(time)
    return (n_data, time_data)

def graphData(data1, data2, data3, graph_name, labels):
    graph1 = graph.plot(data1[0], data1[1], 'rx')
    graph2 = graph.plot(data2[0], data2[1], 'bx')
    graph3 = graph.plot(data3[0], data3[1], 'gx')
    legend1 = mpatches.Patch(color='red', label=labels[0])
    legend2 = mpatches.Patch(color='blue', label=labels[1])
    legend3 = mpatches.Patch(color='green', label=labels[2])
    graph.legend(handles=[legend1, legend2, legend3])
    graph.xscale("log")
    graph.yscale("log")
    graph.xlabel("Problem Size (n)")
    graph.ylabel("Runtime (s)")
    graph.title("Performance of Algorithms")
    graph.grid(True)
    graph.savefig("{}.png".format(graph_name))
    if(SHOW_GRAPHS): graph.show()
    fitCurve(data1, 'r-')
    fitCurve(data2, 'b-')
    fitCurve(data3, 'g-')
    graph.savefig("{}_fitted.png".format(graph_name))
    if(SHOW_GRAPHS): graph.show()


data1 = readData(FILENAME_ROOT.format("binary_random", "naive"))
data2 = readData(FILENAME_ROOT.format("binary_random", "kmp"))
data3 = readData(FILENAME_ROOT.format("binary_random", "bm"))
graphData(data1, data2, data3, "graphs/binary_random_string", ["naive", "kmp", "bm"])

data1 = readData(FILENAME_ROOT.format("binary_regular", "naive"))
data2 = readData(FILENAME_ROOT.format("binary_regular", "kmp"))
data3 = readData(FILENAME_ROOT.format("binary_regular", "bm"))
graphData(data1, data2, data3, "graphs/binary_regular_string", ["naive", "kmp", "bm"])

data1 = readData(FILENAME_ROOT.format("shakespeare", "naive"))
data2 = readData(FILENAME_ROOT.format("shakespeare", "kmp"))
data3 = readData(FILENAME_ROOT.format("shakespeare", "bm"))
graphData(data1, data2, data3, "graphs/shakespeare_string", ["naive", "kmp", "bm"])

data1 = readData(FILENAME_ROOT.format("dna", "naive"))
data2 = readData(FILENAME_ROOT.format("dna", "kmp"))
data3 = readData(FILENAME_ROOT.format("dna", "bm"))
graphData(data1, data2, data3, "graphs/dna_string", ["naive", "kmp", "bm"])

