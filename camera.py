# Class for the camera movement
class Camera:
    def __init__(self, grid, windowSize):
        self.grid = grid
        self.cameraRect = [20, 20, windowSize[0]-20, windowSize[1]-20]
    
    # Move the camera according to its given offset
    def move(self, x, y):
        self.cameraRect[0] += x
        self.cameraRect[1] += y

    # Entirely stop the movement of the camera
    def stop(self):
        self.cameraRect[0] = 0
        self.cameraRect[1] = 0

    # Call the grid's rendering method along with 
    # its camera rect as an argument
    def renderView(self):
        self.grid.renderGrid(self.cameraRect)
