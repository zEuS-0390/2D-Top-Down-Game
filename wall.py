from pygame import sprite, image, transform
from constants import SPRITEIMAGES

# Wall class
class Wall(sprite.Sprite):

    # Constructor
    def __init__(self, blockSize, group, x, y):
        super(Wall, self).__init__(group)
        self.image = image.load(SPRITEIMAGES["WALL"]).convert_alpha()
        self.image = transform.scale(self.image, (blockSize[0], blockSize[1]))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    # Update method
    def update(self, x, y):
        self.rect.x = self.x + x
        self.rect.y = self.y + y