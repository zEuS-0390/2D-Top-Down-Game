from pygame import sprite, image, K_UP, K_DOWN, K_LEFT, K_RIGHT, transform

class Player(sprite.Sprite):
    def __init__(self, grid, camera, group=[]):
        super(Player, self).__init__(group)
        self.grid = grid
        self.camera = camera
        self.directions = [-1, 0]
        self.x, self.y = 320, 240
        self.speed = 4
        self.image = image.load('sprite.png')
        self.image = transform.scale(self.image, (self.grid.blockSize[0], self.grid.blockSize[1]))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def movement(self, key):
        if key == K_UP:
            self.directions[1] = -1
        if key == K_DOWN:
            self.directions[1] = 1
        if key == K_LEFT:
            self.directions[0] = -1
        if key == K_RIGHT:
            self.directions[0] = 1

    def stop(self):
        self.directions = [0, 0]

    def moveSelf(self):
        if self.grid.nodes.nodes[0][0].x+self.x <= 0:
            self.stop()
            self.directions = [1, 0]
        if self.grid.nodes.nodes[0][0].x+self.x >= self.grid.mapSize[1]*self.grid.blockSize[0]:
            self.stop()
            self.directions = [-1, 0]
    
    def move(self):
        self.moveSelf()
        self.x += self.directions[0] * self.speed
        self.y += self.directions[1] * self.speed
        self.grid.nodes.checkPosition(self.grid.nodes.nodes[0][0].x+self.x, self.grid.nodes.nodes[0][0].y+self.y)

    def update(self):
        self.rect.x = self.camera.cameraRect[0]+self.grid.nodes.nodes[0][0].x+self.x
        self.rect.y = self.camera.cameraRect[1]+self.grid.nodes.nodes[0][0].y+self.y
        self.rect.center = self.rect.x, self.rect.y
        self.camera.move(self.directions[0]*self.speed*-1, self.directions[1]*self.speed*-1)
        self.move()
        print(self.grid.nodes.nodes[0][0].x+self.x, self.grid.nodes.nodes[0][0].y+self.y)