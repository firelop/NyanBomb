from pygame_widgets.slider import Slider
import pygame

# Liste des paramètres à implémenter :
#   nbParticules, Vitesse de tir Tourelle
sliders = {}
parameters = ['Nombre de particules', 'Vitesse de tir']
handleColour = [(100, 100, 100), (50, 100, 50)]
colourParams = [(200, 200, 200), (100, 200, 100)]
minParams = [1, 3]
maxParams = [20, 10]
initParams = [8, 3]
SliderPosX, SliderPosY = 50, 50
sliderMenu = pygame.Surface((260, 50*len(parameters)+40))
sliderMenuRect = pygame.Rect(0, 0, sliderMenu.get_width(), sliderMenu.get_height())
sliderRect = pygame.draw.rect(sliderMenu, (255, 255, 255), sliderMenuRect, 10)
i = 0
for parameter in parameters:
    sliders[parameter] = Slider(sliderMenu, 30, 20*((i+1)*2), 200, 20, min=minParams[i], max=maxParams[i], 
                                initial=initParams[i], handleColour=handleColour[i], colour=colourParams[i])
    i += 1

def displayText(content, font, fontSize, rectangleSizeStartX, rectangleSizeStartY, rectangleSizeEndX, rectangleSizeEndY, color):
    font = pygame.font.Font(None, fontSize)
    text = font.render(content, False, color)
    textRect = text.get_rect()
    textRect.center = ((rectangleSizeEndX-rectangleSizeStartX)//2, (rectangleSizeEndY-rectangleSizeStartY)//2)
    return text, textRect


