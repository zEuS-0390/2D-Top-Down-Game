from pathfinding import PathFinding

class Node:
    def __init__(self, x, y, mark=""):
        self.x, self.y = x, y
        self.mark = mark
        self.gCost = 0
        self.hCost = 0
        self.fCost = 0
        self.reset()
    def reset(self):
        self.isStart = False
        self.isEnd = False
        self.isTraversable = True
        self.isVisited = False
        self.isPath = False

class Nodes:
    
    def __init__(self, map, blockSize):
        self.map = map
        self.blockSize = blockSize
        self.nodes = []
        self.path = []
        self.generateNodes()
        self.createFollower()

    def createFollower(self):
        self.startNode = self.nodes[0][0]
        self.startNode.isTraversable = False 
        self.startNode.isStart = True
    
    def findPath(self, endNode):
        pathfinding = PathFinding()
        pathfinding.find(self.startNode, endNode, self.nodes, self.blockSize)
        self.path = pathfinding.retrace(endNode)

    @property
    def getNodes(self):
        return self.nodes

    @property
    def getNodesSize(self):
        return len(self.nodes[0]), len(self.nodes)

    def generateNodes(self):
        for y in range(0, len(self.map)):
            yAxis = []
            for x in range(0, len(self.map[0])):
                yAxis.append(Node(x*self.blockSize[0], y*self.blockSize[1], mark=self.map[y][x]))
            self.nodes.append(yAxis)

    def checkPosition(self, playerX, playerY):
        for y in range(0, len(self.nodes)):
            for x in range(0, len(self.nodes[0])):
                if playerX > self.nodes[y][x].x and playerX < self.nodes[y][x].x+self.blockSize[0] and \
                   playerY > self.nodes[y][x].y and playerY < self.nodes[y][x].y+self.blockSize[1]:
                    self.endNode = self.nodes[y][x]
                    self.endNode.isEnd = True
                    self.findPath(self.endNode)