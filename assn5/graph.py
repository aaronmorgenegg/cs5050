import matplotlib.pyplot as graph
import numpy as np
from scipy.optimize import curve_fit

SHOW_GRAPHS = True

def polyFunc(x, a, b, c):
    return a * np.exp(b*x)+c

def fitCurve(data, color):
    graph.plot(data[0], data[1], color, label="Fitted Curve")
    graph.xscale("log")
    graph.yscale("log")
    graph.xlabel("Problem Size (n)")
    graph.ylabel("Average Runtime (s)")
    graph.title("Performance of Polynomial Algorithms")
    graph.grid(True)

def readData(filename):
    with open(filename, "r") as myfile:
        data = myfile.readlines()
    time_data = []
    n_data = []
    for i in range(len(data)):
        s = data[i].split(",")
        n = int(s[0])
        time = float(s[1])/10
        n_data.append(n)
        time_data.append(time)
    return (n_data, time_data)

def graphData(data1, data2, data3, graph_name):
    graph.plot(data1[0], data1[1], 'rx')
    graph.plot(data2[0], data2[1], 'bx')
    graph.plot(data3[0], data3[1], 'gx')
    graph.xscale("log")
    graph.yscale("log")
    graph.xlabel("Problem Size (n)")
    graph.ylabel("Average Runtime (s)")
    graph.title("Performance of Polynomial Algorithms")
    graph.grid(True)
    graph.savefig("{}.png".format(graph_name))
    if(SHOW_GRAPHS): graph.show()
    fitCurve(data1, 'r-')
    fitCurve(data2, 'b-')
    fitCurve(data3, 'g-')
    graph.savefig("{}_fitted.png".format(graph_name))
    if(SHOW_GRAPHS): graph.show()


schoolbook_data = readData("schoolbook_data.txt")
divide_conquer_data = readData("divide_conquer_data.txt")
fft_data = readData("fft_data.txt")
graphData(schoolbook_data, divide_conquer_data, fft_data, "comparison_graph")

