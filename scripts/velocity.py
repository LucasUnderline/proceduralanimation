from scripts import utils

class Velocity:
    def __init__(self, aceleration):
        self.horizontal = 0
        self.vertical = 0
        self.aceleration = aceleration

    def __getitem__(self, index):
        if index == 0:
            return self.horizontal
        elif index == 1:
            return self.vertical
        else:
            raise IndexError("Index out of range. Use 0 for x and 1 for y.")

    def __iter__(self):
        return iter((self.horizontal, self.y))
    
    def update(self, target_x=0, target_y=0):
        self.horizontal = utils.lerp(self.horizontal, target_x, self.aceleration)
        self.vertical = utils.lerp(self.vertical, target_y, self.aceleration)