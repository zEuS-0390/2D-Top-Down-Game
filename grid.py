from pygame import image, transform, draw, sprite
from node import Nodes
from map import Map
from wall import Wall
from grass import Grass
from constants import SPRITEIMAGES

# Class for the Grid
class Grid:

    # Constructor
    def __init__(self, screen, windowSize, scale):
        self.screen = screen
        self.windowSize = windowSize
        self.scale = scale
        self.setupGrid()

    def setupGrid(self):
        self.gridSize = self.windowSize[0]-20, self.windowSize[1]-20
        self.map = Map('map.txt').load_map()
        self.blockSize = round(self.gridSize[0] / self.scale), \
                         round(self.gridSize[1] / self.scale)
        self.mapSize = len(self.map), len(self.map[0])
        self.nodes = Nodes(self.map, self.blockSize)
        self.walls = sprite.Group()
        self.grasses = sprite.Group()
        for y in range(0, self.mapSize[0]):
            for x in range(0, self.mapSize[1]):
                if self.map[y][x] == "#":
                    Wall(self.blockSize, self.walls, x*self.blockSize[0], y*self.blockSize[1])
                else:
                    Grass(self.blockSize, self.grasses, x*self.blockSize[0], y*self.blockSize[1])
        self.loadImages()

    # Loads images
    def loadImages(self):
        self.grass = image.load(SPRITEIMAGES['GRASS']).convert_alpha()
        self.wall = image.load(SPRITEIMAGES['WALL']).convert_alpha()
        self.grass = transform.scale(self.grass, (self.blockSize[0], self.blockSize[1]))
        self.wall = transform.scale(self.wall, (self.blockSize[0], self.blockSize[1]))

    # Renders the sprites based on the camera
    def renderGrid(self):
        self.walls.draw(self.screen)
        self.grasses.draw(self.screen)

    # Update follower
    def update(self, cameraRect):
        self.walls.update(cameraRect[0], cameraRect[1])
        self.grasses.update(cameraRect[0], cameraRect[1])
        