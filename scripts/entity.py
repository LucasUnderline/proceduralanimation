import math

class entity: 
    def __init__(self, x:int, y:int, velocity:float):
        self.x = x
        self.y = y
        self.velocity = velocity
        
    def move(self, target_x:int, target_y:int)->None:
        if abs(self.x - target_x) <= self.velocity or abs(self.y - target_y) <= self.velocity:
            return
        
        _dx = target_x - self.x
        _dy = target_y - self.y
        _dist = math.hypot(_dx, _dy)
        
        self.x += (_dx / _dist) * self.velocity
        self.y += (_dy / _dist) * self.velocity
        
    def get_pos(self)->tuple:
        return (self.x, self.y)