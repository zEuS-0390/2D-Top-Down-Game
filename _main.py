from follower import Follower
from camera import Camera
from constants import *
from grid import Grid
import pygame

""" *
    * TITLE: Multiple Unit Pathfinding
    *
    * DESCRIPTION: 
    *     This program is a simulation of how pathfinding works with an implementation
    *     of A* algorithm. It can be used in many applications, such as games, AI, etc.
    *     If you want to use this code into your project or you have some questions
    *     regarding into this repository, just kindly email me. Thank you.
    * 
    * EMAIL: zeusjamesbaltazar@gmail.com
    * CREATED BY: zEuS-0390 
    *  """

# Main class
class Main:

    # Constructor
    def __init__(self):
        self.setupGame()
        self.loop()

    # Initialization method
    def setupGame(self):

        # Declarations
        pygame.init()
        self.running = True
        self.FPS = 120
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.scale = SCALE
        self.windowSize = (pygame.display.Info().current_w, \
                           pygame.display.Info().current_h)
        self.grid = Grid(self.screen, self.windowSize, self.scale)
        self.camera = Camera(self.grid, self.windowSize)
        self.clock = pygame.time.Clock()
        self.followers = pygame.sprite.Group()

    # Loop method
    def loop(self):

        # While variable self.running is True, run the loop
        while self.running:

            # Set the frame rate
            self.clock.tick(self.FPS)

            # Handles events
            self.event()

            # Handles updates
            self.update()

            # Handles rendering
            self.render()

    # Event handler
    def event(self):

        for event in pygame.event.get():

            # If the window was closed, change the self.running to False,
            # quit pygame, and exit console
            if event.type == pygame.QUIT:
                self.running = False

            # If the keyboard was pressed
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                # If key R was press, then clear followers sprite group
                if event.key == pygame.K_r:
                    self.followers.empty()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the current position of the mouse relative to the position of the camera
                mouse_POS = (self.camera.cameraRect[0]-pygame.mouse.get_pos()[0])*-1, \
                            (self.camera.cameraRect[1]-pygame.mouse.get_pos()[1])*-1
                
                # Move units to mouse's position
                if event.button == RIGHT_CLICK:
                    paths = self.grid.nodes.requestPath([[follower.x, follower.y] for follower in self.followers], [mouse_POS[0], mouse_POS[1]])
                    for i, follower in enumerate(self.followers):
                        follower.path = paths[i]
                
                # Create follower
                elif event.button == LEFT_CLICK:
                    follower = Follower(ANIMIMAGES['FOLLOWER'], self.grid, self.camera, self.followers, [mouse_POS[0], mouse_POS[1]])

    # Rendering method
    def render(self):
        self.screen.fill((0, 0, 0))
        self.grid.renderGrid()
        self.followers.draw(self.screen)

    # Update method
    def update(self):
        self.camera.slide(pygame.mouse.get_pos(), pygame.mouse.get_focused())
        self.grid.update(self.camera.cameraRect)
        self.followers.update()
        pygame.display.flip()

# Run pygame
if __name__=="__main__":
    main = Main()
    pygame.quit()