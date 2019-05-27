graph1 = {
    0 : [1,2,3],
    1 : [0,2,4],
    2 : [0,1,4],
    3 : [0,4],
    4 : [1,2,3]
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph,k, visited)
    return visited

visited = [dfs(graph1,0, [])]
print(visited)

graph1.keys()
