import math
import numpy as np
from pygame import draw
from scripts.body import Body
from scripts.velocity import Velocity
from scripts import utils

class Chain: 
    def __init__(self, pos:list, mov_speed:float, link_size:int, body_parts:int)->None:
        self.mov_speed = mov_speed
        self.link_size = link_size
        self.velocity = Velocity(0.1)
        
        self.angle_limit_factor = 4
        
        self.body_parts = []
        for each in range(body_parts):
            self.body_parts.append(Body([pos[0] + self.link_size*(each), pos[1]], 0, link_size))
        
        
        
    def move(self, pos:list)->None:
        _dx, _dy, _dt, _ang = utils.calculate_distance_angle(pos, self.body_parts[0].pos)
        _x = (_dx / _dt) * self.mov_speed 
        _y = (_dy / _dt) * self.mov_speed
        
        if abs(_dt) < self.mov_speed:
            return
        
        _ang = utils.constraint_angle(_ang + math.pi, self.body_parts[0].angle, self.angle_limit_factor*16)
        
        self.body_parts[0].angle = utils.normalize_angle(_ang)
        self.velocity.update(_x, _y)
    
    
    def logic(self)->None:  
        self.__update_body([self.body_parts[0].pos[0] + self.velocity[0], 
                            self.body_parts[0].pos[1] + self.velocity[1]])
        self.velocity.update()
    
    
    
    def __update_body(self, pos:list)->None:
        _dx, _dy, _dt, _ang = utils.calculate_distance_angle(self.body_parts[0].pos, pos)
        self.body_parts[0].pos[0] = pos[0]
        self.body_parts[0].pos[1] = pos[1]
        
        
        for each in range(1, len(self.body_parts)):
            _dx, _dy, _dt, _ang = utils.calculate_distance_angle(self.body_parts[each].pos, self.body_parts[each-1].pos)
            if abs(_dt) > 0:
                
                _ang = utils.constraint_angle(_ang, self.body_parts[each - 1].angle, self.angle_limit_factor)
                
                _pos = utils.lengthdir(self.body_parts[each-1].pos, self.link_size, utils.normalize_angle(_ang))
                self.body_parts[each].update([_pos[0], _pos[1]], _ang)
    
    
    
    def draw_chain(self, surface, color:tuple):
        for i, each in enumerate(self.body_parts):
            draw.circle(surface, color, (each.pos[0], each.pos[1]), 8, 0)
            draw.circle(surface, color, (each.pos[0], each.pos[1]), 16, 3)
            if i + 1 < len(self.body_parts):
                _x = self.body_parts[i+1].pos[0]
                _y = self.body_parts[i+1].pos[1]
                draw.line(surface, color, (each.pos[0], each.pos[1]), (_x, _y), 5)