
# Create class, Declare barriers
class AStarGraph(object):
    def __init__(self):
        self.barriers = []

         #Ask for number of Barriers
        noOfBarr=int(input("Enter total number of Barriers : "))

        #Take location of each barrier
        for i in range(noOfBarr):
            x=int(input("Enter row number of Barrier point : "))
            y=int(input("Enter column number of Barrier point : "))

            #Append all these in the list of Barriers
            self.barriers.append([(x, y)])
            #self.barriers.append([(1, 1), (2, 1), (3, 1), (3, 2)])

    #Heuristic Estimation
    def heuristic(self, start, goal):
        D=1
        D2=1
        dx=abs(start[0] - goal[0])
        dy=abs(start[1] - goal[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    #Through these function define map
    def get_vertex_neighbours(self, pos):
        n = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1)]: #(-1, 1), (1, -1), (-1, -1)
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            if x2 < 0 or x2 > 5 or y2 < 0 or y2 > 5:
               continue
            n.append((x2, y2))
        return n

    #calculate move cost
    def move_cost(self, a, b):
        for barriers in self.barriers:
            if b in barriers:
               return 100
        return 1

def AStarSearch(start, end, graph):
        G = {}
        F = {}

        G[start] = 0
        F[start] = graph.heuristic(start, end)

        closedVertices = set()
        openVertices = set([start])
        cameFrom = {}


        while len(openVertices) > 0:
            #Get the vertex in open List with the lowest F score value
            current = None
            currentFscore = None
            for pos in openVertices:
                if current is None or F[pos] < currentFscore:
                    currentFscore = F[pos]
                    current = pos

            #check whether we have reached the goal
            if current == end:
                #retrace our route backward
                path = [current]
                while current in cameFrom:
                     current = cameFrom[current]
                     path.append(current)
                path.reverse()
                return path, F[end]
            openVertices.remove(current)
            closedVertices.add(current)

            for neighbour in graph.get_vertex_neighbours(current):
                if neighbour in closedVertices:
                   continue
                tenatativeG = G[current] + graph.move_cost(current, neighbour)

                if neighbour not in openVertices:
                   openVertices.add(neighbour)
                elif tenatativeG >= G[neighbour]:
                    continue


                cameFrom[neighbour] = current
                G[neighbour] = tenatativeG
                H = graph.heuristic(neighbour, end)     #neighbour will get pass in place of start
                F[neighbour] = G[neighbour] + H  
#main for function call
if __name__ == "__main__":
        graph = AStarGraph()
        s1 = int(input("Enter row number for start point : "))
        s2 = int(input("Enter column number for start point : "))
        g1 = int(input("Enter row number for goal point : "))
        g2 = int(input("Enter column number for goal point : "))
        result, cost = AStarSearch((s1, s2), (g1, g2), graph)
        print("route : ", result)
        print("cost : ", cost)    
