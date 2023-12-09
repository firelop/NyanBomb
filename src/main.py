import pygame
from game import Game
from menu import Menu, Parameters

pygame.init()
monitorInfo = pygame.display.Info()  # Get the resolution of the screen
screen = pygame.display.set_mode((monitorInfo.current_w * .9, monitorInfo.current_h * .9))
pygame.display.set_caption("NyanBomb")  # Set the window title

startMenu = Menu(screen, 0, 0, (screen.get_width(), screen.get_height()), 'black')
startMenu.addText('NyanBomb', 'Aharoni', 100, startMenu.display.get_width(), startMenu.display.get_height() * .95, 'white')
startMenu.addText('Press space to play', 'Aharoni', 30, startMenu.display.get_width(), startMenu.display.get_height() * 1.1, 'white')

settings = Menu(screen, 0, 0, (280, len(Parameters.SLIDERS_DESCRIPTORS)*100), 'black', True)



game = Game(screen, startMenu, settings)
game.play()
pygame.quit()
