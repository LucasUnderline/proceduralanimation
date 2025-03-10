import math
import numpy as np
from scripts.utils import calc_left_point, calc_right_point, calc_tip_points


class Body:
    def __init__(self, pos, angle:int, anchor_radius:float)->None:
        self.pos = [pos[0], pos[1]]
        self.angle = angle
        self.anchor_radius = anchor_radius
        self.left_point = calc_left_point(self.pos, self.angle, self.anchor_radius)
        self.right_point = calc_right_point(self.pos, self.angle, self.anchor_radius)
        
    def update(self, pos, angle:int)->None:
        self.pos = pos
        self.angle = angle
        self.left_point = calc_left_point(self.pos, self.angle, self.anchor_radius)
        self.right_point = calc_right_point(self.pos, self.angle, self.anchor_radius)
    
    def get_tip_points(self)->list:
        return calc_tip_points(self.pos, self.angle, self.anchor_radius)