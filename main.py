from fireworks import Firework
from turret import Turret
import pygame, random

pygame.init()
monitorInfo = pygame.display.Info()  # Get the resolution of the screen
screen = pygame.display.set_mode((monitorInfo.current_w*.9, monitorInfo.current_h*.9))
pygame.display.set_caption("NyanBomb")  # Set the window title
clock = pygame.time.Clock()
running = True
fireworks = []
dt = 0
turret = Turret(screen)
isHoldingClick = False
size = 10
x, y = 0, 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')
    dt = clock.tick(60) / 1000  # Represent the time spent since the last frame

    if pygame.mouse.get_pressed()[0]:
        if not isHoldingClick:
            x, y = pygame.mouse.get_pos()
            isHoldingClick = True
        else:
            size += 50*dt
            pygame.draw.circle(screen, "red", (x, y), size)

    elif isHoldingClick:
        isHoldingClick = False
        fireworks.append(Firework(x, y, screen, size))
        size = 10



    for firework in fireworks:
        firework.updateParticleMovement(dt)
        firework.update()

    turret.render()

    pygame.display.flip()


pygame.quit()
