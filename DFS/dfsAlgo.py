#DFS Algorithm
#Adjacency List (Graph)
graph = {
    'S' : ['B','A'],
    'A' : ['D','C'],
    'B' : ['G','D'],
    'C' : [],
    'D' : ['G', 'C'],
    'G' : []
}

def dfsPath(graph, start, goal):
    stack = [[start]]
    visited = []

    while stack:
        print("Stack : ", stack)
        path = stack.pop(0)
        node = path[-1]
        if node == goal:
            return print("These is the path : ", path)

        children = graph[node]
        for child in children:
            if child not in visited:
                newPath = path + [child]
                stack.insert(0, newPath)
                visited.append(child)

start_node = input("Enter the Source Node : ")[0]    # S = Start Node
goal_node = input("Enter the Goal Node : ")[0]
dfsPath(graph, start_node, goal_node)