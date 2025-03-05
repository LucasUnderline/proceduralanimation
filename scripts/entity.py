import math
from scripts.body import Body
from scripts import utils

class Entity: 
    def __init__(self, x:int, y:int, velocity:float, base_radius:int, body_parts:int)->None:
        self.x = x
        self.y = y
        self.velocity = velocity
        self.base_radius = base_radius
        self.angle = 0
        self.tip_points = utils.calc_tip_points(self.x, self.y, self.angle, self.base_radius)
        
        self.body_parts = []
        for each in range(body_parts): #Create instaces of body part
            self.body_parts.append(Body(self.x + self.base_radius*(each+1), self.y + self.base_radius*(each+1), 0, base_radius))
        
        
        
    def move(self, target_x:int, target_y:int)->None:
        if abs(self.x - target_x) < self.velocity or abs(self.y - target_y) < self.velocity:
            return # If the entity is to near to target position, its dont move
        
        _dx = target_x - self.x #distance horizontal
        _dy = target_y - self.y #distance vertical
        _dt = math.hypot(_dx, _dy) #distance total
        
        self.angle = math.atan2(_dy, _dx) #angle in radians
        
        self.x += (_dx / _dt) * self.velocity #dx/dt to get percentage of velocity have to be applied on that direction
        self.y += (_dy / _dt) * self.velocity
        
        self.tip_points = utils.calc_tip_points(self.x, self.y, self.angle, self.base_radius)
        self.__update_body(self.x, self.y)   
    
    def __update_body(self, x, y)->None:
        _past_body_pos = (x, y)
        for each in range(len(self.body_parts)):
            _dx = self.body_parts[each].x - _past_body_pos[0] # same calc of Move method
            _dy = self.body_parts[each].y - _past_body_pos[1]
            _dt = math.hypot(_dx, _dy)
            _angle = math.atan2(_dy, _dx)
            
            if abs(_dt) > 0: # if the body is near or far of the anchor radius, its get into it
                _f = self.base_radius / _dt # factor to know how much near or far is it
                self.body_parts[each].update(_past_body_pos[0] + (_dx * _f), _past_body_pos[1] + (_dy * _f), _angle)
            
            _past_body_pos = (self.body_parts[each].x, self.body_parts[each].y)