import math
from scripts.utils import calc_left_point, calc_right_point, calc_tip_points


class Body:
    def __init__(self, x:int, y:int, angle:int, anchor_radius:float)->None:
        self.x = x
        self.y = y
        self.angle = angle
        self.anchor_radius = anchor_radius
        self.left_point = calc_left_point(self.x, self.y, self.angle, self.anchor_radius)
        self.right_point = calc_right_point(self.x, self.y, self.angle, self.anchor_radius)
        
    def update(self, x:int, y:int, angle:int)->None:
        self.x = x
        self.y = y
        self.angle = angle
        self.left_point = calc_left_point(self.x, self.y, self.angle, self.anchor_radius)
        self.right_point = calc_right_point(self.x, self.y, self.angle, self.anchor_radius)
    
    def get_tip_points(self)->list:
        return calc_tip_points(self.x, self.y, self.angle, self.anchor_radius)