from pygame import draw
from node import Nodes
from map import Map

# Class for the Grid
class Grid:

    def __init__(self, screen, windowSize, scale):
        self.screen = screen
        self.windowSize = windowSize
        self.gridSize = self.windowSize[0]-20, self.windowSize[1]-20
        self.blockSize = round(self.gridSize[0] / scale), \
                         round(self.gridSize[1] / scale)
        self.map = Map('map.txt').load_map()
        self.mapSize = len(self.map), len(self.map[0])
        self.nodes = Nodes(self.map, self.blockSize)
        self.nodesSize = self.nodes.getNodesSize

    # Update method
    def update(self):
        for y in range(0, len(self.nodes.nodes)):
            for x in range(0, len(self.nodes.nodes[0])):
                self.nodes.nodes[y][x].reset()

    # Renders the grid based on the camera
    def renderGrid(self, cameraRect):
        for y in range(0, self.nodesSize[1]):
            for x in range(0, self.nodesSize[0]):
                tempY = self.nodes.nodes[y][x].y+cameraRect[1]
                tempX = self.nodes.nodes[y][x].x+cameraRect[0]
                if tempX > -self.blockSize[0] and tempX+self.blockSize[0] < self.windowSize[0]+self.blockSize[0] and \
                   tempY > -self.blockSize[1] and tempY+self.blockSize[1] < self.windowSize[1]+self.blockSize[1]:
                    color = (150, 150, 0, 100)
                    if self.nodes.nodes[y][x].mark == "#":
                        color = (0, 150, 0, 100)
                    if self.nodes.nodes[y][x].isVisited:
                        color = (80, 0, 0, 100)
                    if self.nodes.nodes[y][x].isPath:
                        color = (150, 0, 0, 100)
                    draw.rect(self.screen, color, \
                            [tempX, tempY, \
                            self.blockSize[0], self.blockSize[1]])