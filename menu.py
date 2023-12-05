from pygame_widgets.slider import Slider
import pygame

def displayText(content, font, fontSize, width, height, color):
    font = pygame.font.Font(None, fontSize)
    text = font.render(content, False, color)
    textRect = text.get_rect()
    textRect.center = ((width)//2, (height)//2)
    return (text, textRect)


class Menu:
    def __init__(self, x, y, size):
        self.display = pygame.Surface(size)
        self.texts = []
        self.labels = []
        self.sliders = []
        self.rect = pygame.rect.Rect(0, 0, 0, 0)
        self.x = x
        self.y = y
        self.rectColor = 'black'
        self.lineWidth = 0
    
    def addText(self, content, font, fontSize, width, height, color):
        self.texts.append(displayText(content, font, fontSize, width, height, color))
    
    def addSlider(self, x, y, widthSlider, heightSlider, min, max, initial, handleColor, color, 
                  label, font, fontSize, widthLabel, heightLabel, colorLabel):
        self.sliders.append(Slider(self.display, x, y, widthSlider, heightSlider, min=min, max=max, initial=initial, handleColour=handleColor, colour=color))
        self.labels.append(displayText(label, font, fontSize, widthLabel, heightLabel, colorLabel))
        self.addText(str(self.sliders[-1].getValue()), font, fontSize, self.display.get_width()*1.9, y, color)
    
    def addRect(self, color, x, y, width, height, lineWidth):
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.rectColor = color
        self.lineWidth = lineWidth

    def update(self, color):
        self.display.fill(color)

        for text in self.texts:
            self.display.blit(text[0], text[1])

        for label in self.labels:
            self.display.blit(label[0], label[1])


        pygame.draw.rect(self.display, self.rectColor, self.rect, self.lineWidth)


class Parameters:
    LABELS = ['Nombre de particules', 'Vitesse de tir', 'Vent']
    NUMBER_PARTICLES = 0
    SHOOTING_SPEED = 1
    WIND = 2
