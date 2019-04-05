from mygraph import Graph
from myalgorithm import kruskals_algorithm

with open('graph_5.txt') as file:
    line1 = file.readline()
    incidence_matrix = []
    for line in file:
        incidence_matrix.append([int(x) for x in line.split()])

counter = 0
graph = Graph()
new_graph = {}

weight = []
for i in range(len(incidence_matrix)):
    weight.append(incidence_matrix[i][len(incidence_matrix[i]) - 1])

for i in range(len(incidence_matrix[0]) - 1):
    graph.add_vertex(i)

for j in range(len(incidence_matrix)):
    first_one = None
    second_one = None
    counter = 0
    for i in range(len(incidence_matrix[0]) - 1):
        if counter == 0 and incidence_matrix[j][i] == 1:
            first_one = i
            counter = 1
            continue
        if incidence_matrix[j][i] == 1 and counter == 1:
            second_one = i
            counter = 2
        if counter == 2:
            graph.add_edge(first_one, second_one, weight[j])

graph.print_graph()
print('Number of edges: ', graph.num_edges())
print('Number of vertices: ', graph.num_vertices())
print('Vertices: ', graph.vertices())
print('Edges: ', graph.edges())
print('Get vertex: ', graph.get_vertex(2))
print('Get edge: ', graph.get_edge(5, 9))
print('Get adjacents: ', graph.adj_vertices(1))
print(kruskals_algorithm(graph))
