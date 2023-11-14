from fireworks import Firework
import pygame

pygame.init()
monitorInfo = pygame.display.Info()  # Get the resolution of the screen
screen = pygame.display.set_mode((monitorInfo.current_w*.93, monitorInfo.current_h*.93))
pygame.display.set_caption("NyanBomb")  # Set the window title
clock = pygame.time.Clock()
running = True
active = False
fireworks = None
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        print(x, y)
        fireworks = Firework(x, y, screen)
        active = True
    if active:
        fireworks.update()

    pygame.display.flip()

    dt = clock.tick(60) / 1000  # Represent the time spent since the last frame

pygame.quit()