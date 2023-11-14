import pygame
import movement
import physicalObject

pygame.init()
monitorInfo = pygame.display.Info()  # Get the resolution of the screen
screen = pygame.display.set_mode((monitorInfo.current_w*.93, monitorInfo.current_h*.93))
pygame.display.set_caption("NyanBomb")  # Set the window title
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        
    
    pygame.display.flip()

pygame.quit()
