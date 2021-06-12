# Map class
class Map:

    # Constructor
    def __init__(self, filename=""):
        self.filename = filename

    # Load map
    def load_map(self):
        with open(self.filename, 'r') as file:
            map = [y.strip() for y in file.readlines()]
        return map

    # Save map <NOT YET IMPLEMENTED>
    def save_map(self, map):
        with open(self.filename, 'w') as file:
            file.write(map)