from menu import Parameters, Menu
from turret import Turret
from game import playing
import pygame

counting = 0

pygame.init()
monitorInfo = pygame.display.Info()  # Get the resolution of the screen
screen = pygame.display.set_mode((monitorInfo.current_w * .9, monitorInfo.current_h * .9))

game = Menu(0, 0, (screen.get_width(), screen.get_height()))
game.addText('Points : ', 'comicsansms', 60, game.display.get_width()*2-180, 60, 'white')
game.addText(str(counting), 'comicsansms', 60, game.display.get_width()*2-200, 180, 'white')

accueil = Menu(0, 0, (screen.get_width(), screen.get_height()))
accueil.addText('NyanBomb', 'comicsansms', 120, accueil.display.get_width(), accueil.display.get_height(), 'white')
accueil.addText('Made for Numeric and Informatic Sciences', 'comicsansms', 50, accueil.display.get_width(), accueil.display.get_height()+400, 'white')

infos = Menu(0, 0, (320, 100*len(Parameters.LABELS)))
infos.addSlider(30, 50, 220, 20, 1, 20, 8, (100, 100, 100), (200, 200, 200),
                Parameters.LABELS[Parameters.NUMBER_PARTICLES], 'comicsansms', 40, infos.display.get_width(), 50, 'white')
infos.addSlider(30, 125, 220, 20, 1, 10, 3, (50, 100, 50), (100, 200, 100),
                Parameters.LABELS[Parameters.SHOOTING_SPEED], 'comicsansms', 40, infos.display.get_width(), 200, 'white')
infos.addSlider(30, 200, 220, 20, -10, 10, 0, (50, 50, 100), (100, 100, 200),
                Parameters.LABELS[Parameters.WIND], 'comicsansms', 40, infos.display.get_width(), 350, 'white')
infos.addRect('white', 0, 0, infos.display.get_width(), infos.display.get_height(), 10)

pygame.display.set_caption("NyanBomb")  # Set the window title
clock = pygame.time.Clock()
menu = True
play = False
fireworks = []
dt = 0
turret = Turret(game.display)
isHoldingClick = False
size = 5
x, y = 0, 0
allParticles = []
colliding = 0
flowers = []
closestParticle = None

while menu:
    if play:
        menu, play, isHoldingClick, size, fireworks, allParticles, turret, flowers, x, y, closestParticle, counting = playing(
            screen, game, infos, clock, dt, menu, play, isHoldingClick, size, fireworks, allParticles, turret, flowers, x, y, 
            closestParticle, infos.sliders[Parameters.NUMBER_PARTICLES].getValue(), infos.sliders[Parameters.SHOOTING_SPEED].getValue(), 
            infos.sliders[Parameters.WIND].getValue(), counting)
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = True
            elif event.key == pygame.K_ESCAPE:
                menu = False
                play = False

    accueil.update('black')
    screen.blit(accueil.display, (accueil.x, accueil.y))
    dt = clock.tick(120) / 1000  # Represent the time spent since the last frame

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
