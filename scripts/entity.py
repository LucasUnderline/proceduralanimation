import math
from scripts import utils
from pygame import draw
from scripts.chain import Chain
from scripts.velocity import Velocity

class Entity:
    def __init__(self, inicial_position:list, move_speed:float):
        self.move_speed = move_speed
        
        self.spine = Chain(inicial_position, 50, 20)
        self.velocity = Velocity(0.1)
        
    def move(self, pos:list)->None:
        _dx, _dy, _dt, _ang = utils.calculate_distance_angle(pos, self.spine.anchors[0].pos)
        _ang = utils.constraint_angle(_ang+math.pi, self.spine.anchors[0].angle, self.spine.angle_limit_factor*16)
        if abs(_dt) < self.move_speed:
            return
        
        _x = (_dx / _dt) * self.move_speed 
        _y = (_dy / _dt) * self.move_speed
        self.velocity.update(_x, _y)
        self.spine.update_anchor(0, angle=_ang)
        
        
    def logic(self)->None:  
        self.spine.update_chain([self.spine.anchors[0].pos[0] + self.velocity[0], 
                                 self.spine.anchors[0].pos[1] + self.velocity[1]])
        self.velocity.update()
        
    def draw_body(self, surface, color):
        _left_points = []
        _right_points = []
        for i, each in enumerate(self.spine.anchors):
            _left_points.append(each.left_point)
            _right_points.append(each.right_point)
        
        _right_points.reverse()
        _points = utils.catmull_rom_chain(utils.shape_points(self.spine.anchors[0].get_tip_points(-1), _left_points, self.spine.anchors[-1].get_tip_points(), _right_points))
        
        draw.polygon(surface, color, _points, 0)