import math
from pygame import draw
from scripts.body import Body
from scripts import utils

class Chain: 
    def __init__(self, x:int, y:int, mov_speed:float, link_size:int, body_parts:int)->None:
        self.mov_speed = mov_speed
        self.aceleration = 0.1
        self.velocity = [0, 0]
        self.link_size = link_size
        
        self.body_parts = []
        for each in range(body_parts): #Create instaces of body part
            self.body_parts.append(Body(x + self.link_size*(each), y, 0, link_size))
        
        
        
    def move(self, target_x:int, target_y:int)->None:
        if abs(self.body_parts[0].x - target_x) < self.mov_speed or abs(self.body_parts[0].y - target_y) < self.mov_speed:
            return # If the entity is to near to target position, its dont move
        
        _dx = target_x - self.body_parts[0].x #distance horizontal
        _dy = target_y - self.body_parts[0].y #distance vertical
        _dt = math.hypot(_dx, _dy) #distance total
        
        self.angle = math.atan2(_dy, _dx) #angle in radians
        
        _max_x = (_dx / _dt) * self.mov_speed #dx/dt to get percentage of velocity have to be applied on that direction
        _max_y = (_dy / _dt) * self.mov_speed
        
        self.velocity[0] = utils.lerp(self.velocity[0], _max_x, self.aceleration)
        self.velocity[1] = utils.lerp(self.velocity[1], _max_y, self.aceleration)
    
    def logic(self):
        #self.tip_points = utils.calc_tip_points(self.body_parts[0].x, self.body_parts[0].y, self.angle, self.link_size)
        
        self.velocity[0] = utils.lerp(self.velocity[0], 0, self.aceleration)
        self.velocity[1] = utils.lerp(self.velocity[1], 0, self.aceleration)
        self.__update_body(self.body_parts[0].x + self.velocity[0], self.body_parts[0].y + self.velocity[1])
    
    def __update_body(self, x, y)->None:
        self.body_parts[0].x = x
        self.body_parts[0].y = y
        for each in range(1, len(self.body_parts)):
            _dx = self.body_parts[each].x - self.body_parts[each-1].x # same calc of Move method
            _dy = self.body_parts[each].y - self.body_parts[each-1].y
            _dt = math.hypot(_dx, _dy)
            _angle = math.atan2(_dy, _dx)
            
            if abs(_dt) > 0: # if the body is near or far of the anchor radius, its get into it
                _f = self.link_size / _dt # factor to know how much near or far is it
                self.body_parts[each].update(self.body_parts[each-1].x + (_dx * _f), self.body_parts[each-1].y + (_dy * _f), _angle)
    
    def draw_chain(self, surface, color):
        for i, each in enumerate(self.body_parts):
            draw.circle(surface, color, (each.x, each.y), 8, 0)
            draw.circle(surface, color, (each.x, each.y), 16, 3)
            if i + 1 < len(self.body_parts):
                draw.line(surface, color, (each.x, each.y), (self.body_parts[i+1].x, self.body_parts[i+1].y), 5)