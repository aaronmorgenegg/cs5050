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
    return (time_data, n_data)

def graphData(data, graph_name):
    graph.plot(data[0], data[1], 'rx')
    graph.xlabel("Problem Size (n)")
    graph.ylabel("Average Runtime (s)")
    graph.xscale("log")
    graph.yscale("log")
    graph.title("Performance of Schoolbook Algorithm")
    graph.grid(True)
    graph.savefig("{}.png".format(graph_name))
    if(SHOW_GRAPHS): graph.show()


schoolbook_data = readData("schoolbook_data.txt")
graphData(schoolbook_data, "schoolbook_graph")

