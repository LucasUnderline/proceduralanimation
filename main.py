import pygame
import sys
from scripts.entity import Entity
from scripts import utils

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Screen")


C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)


clock = pygame.time.Clock()


mouse_x, mouse_y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
mouse_pressed = False

ent = Entity(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 5, 20, 50)

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
        


    #   ----------------------------------   LOGIC   -----------------------------------
    
    if mouse_pressed:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        ent.move(mouse_x, mouse_y)
    
    #   ---------------------------------  DRAWING  ------------------------------------
    
    screen.fill(C_BLACK)
    
    _left_points = []
    _right_points = []
    _points = []
    
    for each in range(len(ent.body_parts)-1): # Getting all side points of all bodyparts
        _left_points.append(utils.calc_left_point(ent.body_parts[each].x, ent.body_parts[each].y, ent.body_parts[each].angle, 20))
        _right_points.append(utils.calc_right_point(ent.body_parts[each].x, ent.body_parts[each].y, ent.body_parts[each].angle, 20))
    _right_points.reverse()  # reverse because that's have to be drawing from last body part to first
    
    _points = utils.shape_points(ent.tip_points, _left_points, 
                                 ent.body_parts[-1].get_tip_points(), _right_points)
    
    
    pygame.draw.polygon(screen, C_WHITE, _points, 0) #Shape
    
    pygame.draw.circle(screen, C_BLACK, utils.calc_left_point(ent.x, ent.y, ent.angle, 12), 5, 0) #Eye
    pygame.draw.circle(screen, C_BLACK, utils.calc_right_point(ent.x, ent.y, ent.angle, 12), 5, 0) #Eye


    #    ------------------------------ UPDATE SCREEN ----------------------------------
    pygame.display.update()
    clock.tick(120)