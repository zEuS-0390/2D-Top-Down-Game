from player import Player
from camera import Camera
from constants import *
from grid import Grid
import pygame, sys

class Main:
    def __init__(self, width, height):
        pygame.init()
        self.width, self.height = width, height
        self.setupGame()
        self.loop()

    def setupGame(self):
        self.running = True
        self.FPS = 120
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.grid = Grid(self.screen, WINDOWSIZE, SCALE)
        self.camera = Camera(self.grid, WINDOWSIZE)
        self.clock = pygame.time.Clock()

        self.sprites = pygame.sprite.Group()
        self.player = Player(self.grid, self.camera, self.sprites)

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    self.player.movement(event.key)
                if event.type == pygame.KEYUP:
                    self.player.stop()
            self.update()
            self.render()
            self.clock.tick(self.FPS)

    def render(self):
        self.screen.fill((0, 0, 0))
        self.camera.renderView()
        self.sprites.draw(self.screen)

    def update(self):
        self.grid.update()
        self.sprites.update()
        pygame.display.update()

if __name__=="__main__":
    main = Main(*WINDOWSIZE)