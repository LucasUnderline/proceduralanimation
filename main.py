import pygame
import sys
import random
import math
import numpy as np
from scipy.special import comb
from scripts.entity import entity
from scripts.utils import get_left_point, get_right_point, get_tip_points, catmull_rom_chain

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Screen")


C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)


clock = pygame.time.Clock()


mouse_x, mouse_y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
mouse_pressed = False

ent = entity(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 5, 20, 50)

#main loop
while True:
    # -----------------------------------  EVENTS  -------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pressed = True
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_pressed = False
        
    if mouse_pressed:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        ent.move(mouse_x, mouse_y)

    #   ----------------------------------   LOGIC   -----------------------------------
    
    
    #   ---------------------------------  DRAWING  ------------------------------------
    screen.fill(C_BLACK)
    
    _left_points = []
    _right_points = []
    _points = []
    
    for each in range(len(ent.get_body_parts())):
        if each+1 > len(ent.get_body_parts())-1:
            break
        
        _left_points.append(get_left_point(ent.get_body_parts()[each][0], ent.get_body_parts()[each][1], ent.get_body_parts()[each][2], 20))
        _right_points.append(get_right_point(ent.get_body_parts()[each][0], ent.get_body_parts()[each][1], ent.get_body_parts()[each][2], 20))
        
        
    _tip_points = get_tip_points(ent.get_pos()[0], ent.get_pos()[1], ent.get_pos()[2], 20)
    _points += _tip_points

    _points += _left_points
    
    _tip_points = get_tip_points(ent.get_body_parts()[-1][0], ent.get_body_parts()[-1][1], ent.get_body_parts()[-1][2], 20)
    _points += _tip_points
    
    _right_points.reverse()
    _points += _right_points
    
    pygame.draw.lines(screen, C_WHITE, True, _points, 5)
    
    pygame.draw.circle(screen, C_WHITE, get_left_point(ent.get_body_parts()[0][0], ent.get_body_parts()[0][1], ent.get_body_parts()[0][2], 12), 5, 0)
    pygame.draw.circle(screen, C_WHITE, get_right_point(ent.get_body_parts()[0][0], ent.get_body_parts()[0][1], ent.get_body_parts()[0][2], 12), 5, 0)


    #    ------------------------------ UPDATE SCREEN ----------------------------------
    pygame.display.update()
    clock.tick(120)