import pygame, pygame_widgets
from pygame_widgets.slider import Slider

pygame.init()
monitorInfo = pygame.display.Info()
screen = pygame.display.set_mode((monitorInfo.current_w * .9, monitorInfo.current_h * .9))
clock = pygame.time.Clock()
run = True
sliderTest = Slider(screen, 50, 100, 200, 30, max=20, handleColour=(100, 100, 100), colour=(200, 200, 200))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    events = pygame.event.get()
    screen.fill((50, 50, 50))
    pygame.draw.circle(screen, (150, 150, 150), (screen.get_width()//2, screen.get_height()//2), sliderTest.getValue()*10)

    pygame_widgets.update(events)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()