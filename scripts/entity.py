import math

class entity: 
    def __init__(self, x:int, y:int, velocity:float, base_radius:int, body_parts:int)->None:
        self.x = x
        self.y = y
        self.velocity = velocity
        self.base_radius = base_radius
        
        self.body_parts = []
        for each in range(body_parts):
            self.body_parts.append([self.x + self.base_radius*(each+1), self.y + self.base_radius*(each+1)]) #X, Y, Angle
        
        
    def move(self, target_x:int, target_y:int)->None:
        if abs(self.x - target_x) <= self.velocity or abs(self.y - target_y) <= self.velocity:
            return
        
        _dx = target_x - self.x
        _dy = target_y - self.y
        _dist = math.hypot(_dx, _dy)
        
        self.x += (_dx / _dist) * self.velocity
        self.y += (_dy / _dist) * self.velocity
        
        
        
        _past_body_pos = (self.x, self.y)
        for each in range(len(self.body_parts)):
            _dx = self.body_parts[each][0] - _past_body_pos[0]
            _dy = self.body_parts[each][1] - _past_body_pos[1]
            _dt = math.hypot(_dx, _dy)
            
            if _dt > 0:
                _f = self.base_radius / _dt
                self.body_parts[each][0] = _past_body_pos[0] + (_dx * _f)
                self.body_parts[each][1] = _past_body_pos[1] + (_dy * _f)
            
            _past_body_pos = (self.body_parts[each][0], self.body_parts[each][1])
        
    def get_pos(self)->tuple:
        return (self.x, self.y)
    
    def get_body_parts_pos(self)->list:
        return self.body_parts
    