def kruskals_algorithm(graph):
    result = []
    i = 0
    e = 0
    new_graph = sorted(graph.edges(), key=lambda item: item[2])
    parent_vertex = []
    rank = []
    for vertex in range(graph.num_vertices()):
        parent_vertex.append(vertex)
        rank.append(0)

    while e < graph.num_vertices() - 1:

        u, v, w = new_graph[i]
        i = i + 1
        a = graph.find(parent_vertex, u)
        z = graph.find(parent_vertex, v)

        if a != z:
            e = e + 1
            result.append([u, v, w])
            graph.union(parent_vertex, rank, a, z)

    for u, v, weight in result:
        print(str(u) + " -- " + str(v) + " == " + str(weight))
