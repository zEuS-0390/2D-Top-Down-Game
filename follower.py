from pygame import sprite, image, transform
from math import atan2, pi

# Follower class
class Follower(sprite.Sprite):

    # Constructor
    def __init__(self, animImages, grid, camera, group, initPos):
        super(Follower, self).__init__(group)
        self.grid = grid
        self.camera = camera
        self.direction = {}
        self.x, self.y = initPos[0], initPos[1]
        self.loadImages(animImages)
        self.image = self.direction['DOWN']
        self.setupFollwower()

    def loadImages(self, animImages):
        for path in animImages:
            img = image.load(animImages[path]).convert_alpha()
            img = transform.scale(img, self.grid.blockSize)
            img.set_colorkey([255, 174, 201])
            self.direction[path] = img
    
    # Setup sprite
    def setupFollwower(self):
        self.path = []
        self.speed = 2
        self.moveDir = [0, 0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

    # Move the sprite based on the given position
    def movement(self, targetPos):

        self.moveDir = [0, 0]

        if self.x < targetPos[0] and self.x < targetPos[0]+20:
            self.moveDir[0] = self.speed
        elif self.x > targetPos[0] and self.x > targetPos[0]-20:
            self.moveDir[0] = -self.speed
        
        if self.y < targetPos[1] and self.y < targetPos[1]+20:
            self.moveDir[1] = self.speed
        elif self.y > targetPos[1] and self.y > targetPos[1]-20:
            self.moveDir[1] = -self.speed

        self.x += self.moveDir[0]
        self.y += self.moveDir[1]

    # Move the follower
    def move(self):
        if len(self.path) > 0:
            if not self.collision(self.path[0]):
                self.movement(self.path[0])
                self.getAngle(self.path[0])
            else:
                self.path.pop(0)
        else:
            self.image = self.direction['DOWN']

    # This is for the target point. It will check if this object collides with the point
    def collision(self, point):
        if point[0] < self.x + round(self.rect.width/2) and point[0] > self.x - round(self.rect.width/2) and \
           point[1] < self.y + round(self.rect.height/2) and point[1] > self.y - round(self.rect.height/2):
           return True
        return False

    # Change image depending on the angle pointing to the target
    def getAngle(self, point):

        x = point[0] - self.x
        y = point[1] - self.y
        angle = atan2(x, y) * (180/pi)

        if angle <= 15 and angle > -15:
            self.image = self.direction['DOWN']
        elif angle <= -15 and angle > -75:
            self.image = self.direction['DOWNLEFT']
        elif angle <= -75 and angle > -105:
            self.image = self.direction['LEFT']
        elif angle <= -105 and angle > -165:
            self.image = self.direction['UPLEFT']
        elif angle <= -165 and angle > 165:
            self.image = self.direction['UP']
        elif angle <= 165 and angle > 105:
            self.image = self.direction['UPRIGHT']
        elif angle <= 105 and angle > 75:
            self.image = self.direction['RIGHT']
        elif angle <= 75 and angle > 15:
            self.image = self.direction['DOWNRIGHT']

    # Simply draw the image
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    # Update follower
    def update(self):
        self.rect.x = self.camera.cameraRect[0]+self.x
        self.rect.y = self.camera.cameraRect[1]+self.y
        self.rect.center = self.rect.x, self.rect.y
        self.move()