import matplotlib.pyplot as graph

SHOW_GRAPHS = True

def readData(filename):
    with open(filename, "r") as myfile:
        data = myfile.readlines()
    time_data = []
    n_data = []
    for i in range(len(data)):
        s = data[i].split(",")
        n = s[0]
        time = float(s[1])/10
        n_data.append(n)
        time_data.append(time)
    return (n_data, time_data)

def graphData(data1, data2, graph_name):
    graph.plot(data1[0], data1[1], 'rx')
    graph.plot(data2[0], data2[1], 'bx')
#    graph.xscale("log")
    graph.yscale("log")
    graph.xlabel("Problem Size (n)")
    graph.ylabel("Average Runtime (s)")
    graph.title("Performance of Polynomial Algorithms")
    graph.grid(True)
    graph.savefig("{}.png".format(graph_name))
    if(SHOW_GRAPHS): graph.show()


schoolbook_data = readData("schoolbook_data.txt")
divide_conquer_data = readData("divide_conquer_data.txt")
graphData(schoolbook_data, divide_conquer_data, "comparison_graph")

