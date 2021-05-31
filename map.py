class Map:
    def __init__(self, filename=""):
        self.filename = filename
    def load_map(self):
        with open(self.filename, 'r') as file:
            map = [y.strip() for y in file.readlines()]
        return map