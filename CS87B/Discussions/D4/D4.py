#Name: Alfonso Del Rosario
#Submission Date: 10/16/2021
#Discussion 4

#Here I tried to familiarize myself with plotting familiar functions from
#math courses that I have taken, because it seems like it would a useful
#tool to have in the future.

import matplotlib.pyplot as plt
import numpy as np

def sq(x):
    return x**2

def cube(x):
    return x**3

def main():

    domain_size = 10

    x = np.linspace(-domain_size, domain_size, domain_size * 5)

    y=[]
    z=[]

    for i in range (0, len(x)): 
        y.append(sq(x[i]))
    for i in range (0, len(x)):
        z.append(cube(x[i]))

    f, (graph, graph_2) = plt.subplots(2)

    graph.spines['right'].set_color('none')
    graph.spines['left'].set_position('center')
    graph.spines['right'].set_position('center')

    graph_2.spines['right'].set_color('none')
    graph_2.spines['left'].set_position('center')
    graph_2.spines['right'].set_position('center')
    graph_2.spines['bottom'].set_position('center')
    graph_2.spines['top'].set_position('zero')

    graph.plot(x,y)
    graph_2.plot(x,z)

    plt.show()

main()