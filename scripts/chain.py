import math
import numpy as np
from pygame import draw
from scripts.anchors import Anchors
from scripts.velocity import Velocity
from scripts import utils

class Chain: 
    def __init__(self, pos:list, link_size:int, anchors:int)->None:
        self.link_size = link_size
        
        self.angle_limit_factor = 4
        
        self.anchors = []
        for each in range(anchors):
            self.anchors.append(Anchors([pos[0] + self.link_size*(each), pos[1]], 0, link_size/3))
        
        
    def update_chain(self, pos:list)->None:
        _dx, _dy, _dt, _ang = utils.calculate_distance_angle(self.anchors[0].pos, pos)
        _ang = utils.constraint_angle(_ang + math.pi, self.anchors[0].angle, self.angle_limit_factor*16)
        self.update_anchor(0, pos=pos)
        
        
        for each in range(1, len(self.anchors)):
            _dx, _dy, _dt, _ang = utils.calculate_distance_angle(self.anchors[each].pos, self.anchors[each-1].pos)
            if abs(_dt) > 0:
                
                _ang = utils.constraint_angle(_ang, self.anchors[each - 1].angle, self.angle_limit_factor)
                
                _pos = utils.lengthdir(self.anchors[each-1].pos, self.link_size, utils.normalize_angle(_ang))
                self.anchors[each].update([_pos[0], _pos[1]], _ang)
    
    def update_anchor(self, anchor_index, pos=None, angle=None):
        if anchor_index > len(self.anchors)-1:
            anchor_index = len(self.anchors)-1
        if pos == None:
            pos = self.anchors[anchor_index].pos
        if angle == None:
            angle = self.anchors[anchor_index].angle
        
        self.anchors[anchor_index].update(pos, angle)
        
    
    def draw_chain(self, surface, color:tuple):
        for i, each in enumerate(self.anchors):
            draw.circle(surface, color, (each.pos[0], each.pos[1]), 8, 0)
            draw.circle(surface, color, (each.pos[0], each.pos[1]), 16, 3)
            if i + 1 < len(self.anchors):
                _x = self.anchors[i+1].pos[0]
                _y = self.anchors[i+1].pos[1]
                draw.line(surface, color, (each.pos[0], each.pos[1]), (_x, _y), 5)