class Graph(object):
    def __init__(self, _graph=None):
        self.graph = {}

    def print_graph(self):
        for v in self.graph.keys():
            print("Vertex:", v, " --> ", self.graph[v])
        return self.graph

    def num_vertices(self):
        return len(list(self.graph.keys()))

    def num_edges(self):
        return len(self.edges())

    def add_vertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = {}

    def add_edge(self, u, v, w=None):
        if u not in self.graph.keys():
            self.add_vertex(u)
        if v not in self.graph[u]:
            self.graph[u][v] = w
        if u not in self.graph[v]:
            self.graph[v][u] = w

    def get_vertex(self, v):
        if v in self.graph:
            return self.graph[v]
        else:
            return None

    def get_edge(self, u, v):
        try:
            if u in self.graph[v] or v in self.graph[u]:
                exists = 'Edge (' + str(u) + ', ' + str(v) + ') exists'
                return exists
        except:
            return "Edge (" + str(u) + ', ' + str(v) + ") doesn't exists"

    def vertices(self):
        return list(self.graph.keys())

    def edges(self):
        edges = []
        for vertex in self.graph:
            for neighbour_vertex in self.graph[vertex]:
                if [neighbour_vertex, vertex, self.graph[vertex][neighbour_vertex]] not in edges:
                    edges.append([vertex, neighbour_vertex, self.graph[vertex][neighbour_vertex]])
        return edges

    def adj_vertices(self, v):
        suc = list(self.graph[v])
        res = []
        for k in self.graph.keys():
            if v in self.graph[k]:
                res.append(k)
        for p in suc:
            if p not in res:
                res.append(p)
        return res

    def find(self, parent_vertex, i):
        if parent_vertex[i] == i:
            return i
        return self.find(parent_vertex, parent_vertex[i])

    def union(self, parent_vertex, rank, a, z):
        root_a = self.find(parent_vertex, a)
        root_z = self.find(parent_vertex, z)

        if rank[root_a] < rank[root_z]:
            parent_vertex[root_a] = root_z
        elif rank[root_a] > rank[root_z]:
            parent_vertex[root_z] = root_a
        else:
            parent_vertex[root_z] = root_a
            rank[root_a] += 1

    def __len__(self):
        return len(self.graph)

    def __iter__(self):
        return iter(self.graph.values())
