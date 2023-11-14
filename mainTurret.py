import pygame
from turret import Turret

pygame.init()
monitorInfo = pygame.display.Info()  # Get the resolution of the screen
screen = pygame.display.set_mode((monitorInfo.current_w*.90, monitorInfo.current_h*.90))
pygame.display.set_caption("NyanBomb")  # Set the window title
clock = pygame.time.Clock()
running = True
dt = 0
turret = Turret(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(60) / 1000  # Represent the time spent since the last frame
    screen.fill((0,0,0))
    turret.render()
    pygame.display.flip()

pygame.quit()
