from pathfinding import PathFinding

# Node class
class Node:

    # Constructor
    def __init__(self, x, y, mark=""):
        self.x, self.y = x, y
        self.mark = mark
        self.reset()

    # Reset the node
    def reset(self):
        self.gCost = 0
        self.hCost = 0
        self.fCost = 0
        self.isStart = False
        self.isEnd = False
        self.isTraversable = True
        self.parent = None

# Nodes class
class Nodes:
    
    # Constructor
    def __init__(self, map, blockSize):
        self.map = map
        self.blockSize = blockSize
        self.nodes = []
        self.pathfinding = PathFinding()
        self.generateNodes()
        self.generateWalls()

    # Set start node from the given grid coordintae
    def setStartNode(self, x, y):
        pos = self.checkPosition(x, y)
        node = self.nodes[pos[1]][pos[0]]
        node.isStart = True
        node.isTraversable = False
        return node

    # Set end node from the given grid coordintae
    def setEndNode(self, x, y):
        pos = self.checkPosition(x, y)
        node = self.nodes[pos[1]][pos[0]]
        node.isEnd = True
        return node

    # Uses queue system to avoid simultaneous requests
    def requestPath(self, multiStartPos, endPos):
        paths = []
        size = len(multiStartPos)
        for i in range(0, size):
            paths.append(self.findPath(multiStartPos[i], endPos))
            self.reset()
        return paths

    # Uses A-star algorithm to find the path for special nodes
    def findPath(self, start, end):
        try:
            startNode = self.setStartNode(*start)
            endNode = self.setEndNode(*end)
            self.pathfinding.find(startNode, endNode, self.nodes, self.blockSize)
            path = self.pathfinding.retrace(endNode)
            return path
        except:
            return []

    # Reset all nodes
    def reset(self):
        for y in range(0, len(self.nodes)):
            for x in range(0, len(self.nodes[0])):
                self.nodes[y][x].reset()
        self.generateWalls()

    # Create walls by determining the symbol from the map
    def generateWalls(self):
        for y in range(0, len(self.nodes)):
            for x in range(0, len(self.nodes[0])):
                if self.nodes[y][x].mark == "#":
                    self.nodes[y][x].isTraversable = False

    @property
    def getNodesSize(self):
        return len(self.nodes[0]), len(self.nodes)

    # Generate nodes
    def generateNodes(self):
        for y in range(0, len(self.map)):
            yAxis = []
            for x in range(0, len(self.map[0])):
                yAxis.append(Node(x*self.blockSize[0], y*self.blockSize[1], mark=self.map[y][x]))
            self.nodes.append(yAxis)

    # Check the current sprites position in node coordinates
    def checkPosition(self, X, Y):
        for y in range(0, len(self.nodes)):
            for x in range(0, len(self.nodes[0])):
                if X >= self.nodes[y][x].x and X <= self.nodes[y][x].x+self.blockSize[0] and \
                   Y >= self.nodes[y][x].y and Y <= self.nodes[y][x].y+self.blockSize[1]:
                    return x, y