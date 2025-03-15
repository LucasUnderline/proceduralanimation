import pygame
import sys
from scripts.chain import Chain
from scripts import utils

pygame.init()
pygame.font.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Screen")

C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_RED = (255, 0, 0)

clock = pygame.time.Clock()

mouse_x, mouse_y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
mouse_pressed = False

spine = Chain((SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 8, 50, 20)
font = pygame.font.Font(None, 36)

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
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()

    #   ----------------------------------   LOGIC   -----------------------------------
    
    if mouse_pressed:
        spine.move(pygame.mouse.get_pos())
        
    spine.logic()
    
    #   ---------------------------------  DRAWING  ------------------------------------
    
    screen.fill(C_BLACK)
    spine.draw_chain(screen, C_WHITE)

    #    ------------------------------ UPDATE SCREEN ----------------------------------
    
    pygame.display.update()
    clock.tick(120)