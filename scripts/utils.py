import pygame
import math
import numpy as np

def catmull_rom_chain(points, num_points=20):
    if len(points) < 4:
        return points  # Sem curva se houver menos de 4 pontos

    curve = []
    rng = np.linspace(0, 1, num_points)  # Pré-calcula os valores de t

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



def get_left_point(x:int, y:int, angle:float, radius:int)->tuple:
    _left_point = (x + (radius * math.cos(angle - math.pi/2)),
                  y + (radius * math.sin(angle - math.pi/2)))
        
    return _left_point

def get_right_point(x:int, y:int, angle:float, radius:int)->tuple:
    _right_point = (x + (radius * math.cos(angle + math.pi/2)), 
                   y + (radius * math.sin(angle + math.pi/2)))
    
    return _right_point

def get_tip_points(x:int, y:int, angle:float, radius:int)->list:
    _tip_point = (x + (radius * math.cos(angle)), 
                  y + (radius * math.sin(angle)))
    
    _left_tip_point = (x + (radius * math.cos(angle - (math.pi / 4))), 
                       y + (radius * math.sin(angle - (math.pi / 4))))
    
    _right_tip_point = (x + (radius * math.cos(angle + (math.pi / 4))), 
                        y + (radius * math.sin(angle + (math.pi / 4))))
    
    _left_point = get_left_point(x, y, angle, radius)
    
    _right_point = get_right_point(x, y, angle, radius)
        
    return [_left_point, _left_tip_point, _tip_point, _right_tip_point, _right_point]