def kruskals_algorithm(graph):
    result = []
    ind_graph = 0
    result_count = 0

    sorted_edges = sorted(graph.edges(), key=lambda part: part[2])
    parent_vertex = [vertex for vertex in range(graph.num_vertices())]
    rank = [i for i in range(graph.num_vertices())]

    while result_count < graph.num_vertices() - 1:
        if ind_graph >= len(sorted_edges):
            break

        u, v, w = sorted_edges[ind_graph]
        first = graph.find(parent_vertex, u)
        last = graph.find(parent_vertex, v)
        ind_graph += 1

        if first != last:
            result_count = result_count + 1
            result.append([u, v, w])
            graph.union(parent_vertex, rank, first, last)

    for u, v, weight in result:
        print(str(u) + " -- " + str(v) + " == " + str(weight))
