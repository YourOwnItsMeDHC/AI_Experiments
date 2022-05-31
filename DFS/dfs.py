#DFS Algorithm

#Adjacency List (Graph)
graph = {
    'A' : ['B','C'],
    'B' : ['E','D'],
    'E' : ['C','D','F'],
    'C' : [],
    'D' : ['F'],
    'F' : []
}

#Set to keep track of visited nodes
visited = set()

#Define function for DFS
def dfs(visited, graph, node):

    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            print("Neighbour of " + node + " is now " + neighbour)
            dfs(visited, graph, neighbour)

#Function Call
dfs(visited, graph, 'A')