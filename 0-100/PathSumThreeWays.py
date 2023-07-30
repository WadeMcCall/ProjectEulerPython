class Graph:
    def __init__(self, matrix):
        self.matrix = []
        for row in range(len(matrix)):
            self.matrix.append([])
            for column in range(len(matrix[row])):
                node = Node(matrix[row][column])
                node.row = row
                node.column = column
                self.matrix[row].append(node)

    def getNeighbors(self, row, column):
        neighbors = []
        if row > 0:
            neighbors.append(self.matrix[row-1][column])
        if row < len(self.matrix) - 1:
            neighbors.append(self.matrix[row+1][column])
        if column < len(self.matrix[0]) - 1:
            neighbors.append(self.matrix[row][column+1])
        return neighbors

    def __str__(self):
        ret = ""
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                ret += str(self.matrix[row][column].dist) + " "
            ret += "\n"
        return ret

    def __repl__(self):
        return str(self)

class Node:
    def __init__(self, value):
        self.value = value
        self.dist = 1e9
        self.prev = None
        self.row = None
        self.column = None

    def __str__(self):
        return str(self.dist)
    
    def __repl__(self):
        return str(self)
        

def getGraph():
    f = open("data/Matrix82.txt", "r")
    matrix = []
    for line in f:
        matrix.append([int(x) for x in line.split(",")])
    graph = Graph(matrix)
    return graph

def dijkstra(graph, startRow):
    graph.matrix[startRow][0].dist = graph.matrix[startRow][0].value
    queue = []
    for row in range(len(graph.matrix)):
        for column in range(len(graph.matrix[row])):
            queue.append(graph.matrix[row][column])
    while(len(queue) > 0):
        queue.sort(key=lambda x: x.dist)
        u = queue.pop(0)
        for neighbor in graph.getNeighbors(u.row, u.column):
            alt = u.dist + neighbor.value
            if(alt < neighbor.dist):
                neighbor.dist = alt
                neighbor.prev = u

def main():
    graph = getGraph()
    for i in range(len(graph.matrix[0])):
        dijkstra(graph, i)
    min = 1e9
    for node in [i[-1] for i in graph.matrix]:
        if(node.dist < min):
            min = node.dist
    print(min)
    return

if __name__ == '__main__':
    main()