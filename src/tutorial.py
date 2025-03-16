import graph as g

edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5)]

G = g.create_graph(edges)


print(g.get_degree(G, 2))

print(g.dfs_traversal(G, 1))


print(g.bfs_traversal(G, 1))

print(g.find_shortest_path(G, 1, 4))


g.visualize_graph(G)