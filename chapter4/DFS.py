def dfs(graph,start):
    start.visited = True
    for element in graph[start]:
        if element.visited == False:
            dfs(graph,element)
    return start.visited
