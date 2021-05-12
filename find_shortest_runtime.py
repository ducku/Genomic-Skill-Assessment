# problem can be represented using an acyclic graph, using nodes and vectors
# we can represent each relied on task using an edge
# the longest path can be calculated by adding up all the time required to complete the path

from graph_tool.all import *
import json
import sys
import numpy as np


options = "f"

long_options = "files"

arguments = sys.argv[1:]

options, values = getopt.getopt(arguments, options, long_options)

f = open(values[0])

dictionary = json.load(f)

# use graph to keep track of directed edges and tasks
g = Graph()
g.add_vertex(len(dictionary)) # add vertex equal to number of tasks
vprop_time =  g.new_vertex_property("int") # each vertex has a time(int)
vprop_cpu = g.new_vertex_property("int") # each vertex has a cpu(int)
vprop_visited = g.new_vertex_property("bool")

d = defaultdict(list)
task_index = 0
for task in dictionary:
    
    if "TASK" in task["relies_on"]:
        v = g.vertex[task_index]
        vprop_time[v] = task["time"] # assign time value
        vprop_cpu[v] = task["cpu"] # assign cpu value

        # add edge if task is relied on
        e = g.add_edge(g.vertex(int((task["relies_on"])[4:])), g.vertex(task_index))

    task_index++


# cpu occupation
available_cpu = 16

def complete_task(g, available_cpu):
    
