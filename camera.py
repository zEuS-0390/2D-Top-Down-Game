# Class for the camera movement
class Camera:

    # Constructor
    def __init__(self, grid, windowSize):
        self.grid = grid
        self.windowSize = windowSize
        self.speed = 4
        self.cameraRect = [0, 0, windowSize[0]-20, windowSize[1]-20]
    
    # Move the camera according to its given offset
    def move(self, x, y):
        self.cameraRect[0] += x
        self.cameraRect[1] += y

    # Slide the camera when you move your mouse
    def slide(self, mpos, focused):
        if focused:
            if mpos[0] >= self.windowSize[0]-(self.windowSize[0] / 10):
                self.move(-self.speed, 0)
            if mpos[0] <= self.windowSize[0] / 10:
                self.move(self.speed, 0)
            if mpos[1] <= self.windowSize[1]-(self.windowSize[1] / 10):
                self.move(0, self.speed)
            if mpos[1] >= self.windowSize[1] / 10:
                self.move(0, -self.speed)

    # Entirely stop the movement of the camera
    def stop(self):
        self.cameraRect[0] = 0
        self.cameraRect[1] = 0