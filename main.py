import pygame
import sys
import random
from scripts.entity import entity

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Screen")


C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)


clock = pygame.time.Clock()


mouse_x, mouse_y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
mouse_pressed = False

ent = entity(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 2)

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
        
        elif event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
        
    if mouse_pressed:
        ent.move(mouse_x, mouse_y)

    #   ----------------------------------   LOGIC   -----------------------------------
    
    
    #   ---------------------------------  DRAWING  ------------------------------------
    screen.fill(C_BLACK)
    pygame.draw.circle(screen, C_WHITE, (ent.get_pos()[0], ent.get_pos()[1]), 40, 3)


    pygame.display.update()
    clock.tick(120)