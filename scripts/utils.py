import pygame
import math
import numpy as np


def catmull_rom_chain(points, num_points=20): # Smooth line curves algoritm, unused for now
    if len(points) < 4:
        return points
    curve = []
    rng = np.linspace(0, 1, num_points)
    for i in range(1, len(points) - 2):
        P0, P1, P2, P3 = points[i - 1], points[i], points[i + 1], points[i + 2]
        for t in rng:
            t2, t3 = t * t, t * t * t
            x = int(0.5 * (
                (2 * P1[0]) + (-P0[0] + P2[0]) * t +
                (2 * P0[0] - 5 * P1[0] + 4 * P2[0] - P3[0]) * t2 +
                (-P0[0] + 3 * P1[0] - 3 * P2[0] + P3[0]) * t3))
            y = int(0.5 * (
                (2 * P1[1]) + (-P0[1] + P2[1]) * t +
                (2 * P0[1] - 5 * P1[1] + 4 * P2[1] - P3[1]) * t2 +
                (-P0[1] + 3 * P1[1] - 3 * P2[1] + P3[1]) * t3))
            curve.append((x, y))
    return curve



def calc_left_point(pos, angle:float, radius:int)->tuple:
    _left_point = (pos[0] + (radius * math.cos(angle - math.pi/2)),
                   pos[1] + (radius * math.sin(angle - math.pi/2)))
        
    return _left_point

def calc_right_point(pos, angle:float, radius:int)->tuple:
    _right_point = (pos[0] + (radius * math.cos(angle + math.pi/2)), 
                    pos[1] + (radius * math.sin(angle + math.pi/2)))
    
    return _right_point

def calc_tip_points(pos, angle:float, radius:int)->list:
    _tip_point = (pos[0] + (radius * math.cos(angle)), 
                  pos[1] + (radius * math.sin(angle)))

    _left_tip_point = (pos[0] + (radius * math.cos(angle - (math.pi / 4))), 
                       pos[1] + (radius * math.sin(angle - (math.pi / 4))))
    
    _right_tip_point = (pos[0] + (radius * math.cos(angle + (math.pi / 4))), 
                        pos[1] + (radius * math.sin(angle + (math.pi / 4))))
    
    _left_point = calc_left_point(pos, angle, radius)
    _right_point = calc_right_point(pos, angle, radius)
        
    return [_left_point, _left_tip_point, _tip_point, _right_tip_point, _right_point]

def shape_points(*args):
    _points = []
    for each in args:
        _points += each
    
    return _points

def lerp(val1, val2, factor):
    return (1 - factor) * val1 + factor * val2

def calculate_distance_angle(target: list, source: list
                             ) -> tuple[float, float, float, float]:
    
        dx = target[0] - source[0]
        dy = target[1] - source[1]
        dist = math.hypot(dx, dy)
        angle = normalize_angle(math.atan2(dy, dx))
        return dx, dy, dist, angle
    
def lengthdir(pos, dist, angle):
    x = dist * math.cos(angle)
    y = dist * math.sin(angle)
    return pos[0]+ x, pos[1] + y

def normalize_angle(angle):
    return (angle + math.pi) % (2 * math.pi) - math.pi

def subtract_vectors(list1, list2):
    a = list1[0] - list2[0]
    b = list1[1] - list2[1]
    return a, b

def unwrap_angle(current_angle, prev_angle):
    while current_angle - prev_angle > math.pi:
        current_angle -= 2 * math.pi
    while current_angle - prev_angle < -math.pi:
        current_angle += 2 * math.pi
    return current_angle

def unwrap_one_angle(current_angle):
    while current_angle > math.pi:
        current_angle -= 2 * math.pi
    while current_angle < -math.pi:
        current_angle += 2 * math.pi
    return current_angle

def constraint_angle(angle, anchor, limit_factor):
    prev_angle = anchor
    angle = unwrap_angle(angle, prev_angle)

    sup_limit = prev_angle + (math.pi / limit_factor)
    inf_limit = prev_angle - (math.pi / limit_factor)
    
    if angle > sup_limit:
        angle = sup_limit
    elif angle < inf_limit:
        angle = inf_limit
        
    return angle

def lerp_angle(angle1, angle2, t):
    delta = (angle2 - angle1 + math.pi) % (2 * math.pi) - math.pi
    if abs(delta) < 1e-6:
        return angle2

    interpolated_angle = angle1 + delta * t
    return (interpolated_angle + math.pi) % (2 * math.pi) - math.pi