from typing import List, Tuple

import pygame_widgets
from pygame_widgets.slider import Slider
import pygame


def displayText(content, font, fontSize, width, height, color):
    font = pygame.font.SysFont(font, fontSize)
    text = font.render(content, True, color)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 2)
    return [text, textRect]


class Menu:
    def __init__(self, screen, x, y, size, color, isSettings=False):
        self.display = pygame.Surface(size)
        self.display.set_colorkey((0, 0, 0))
        self.texts = []
        self.labels = []
        self.sliders = []
        self.rect = pygame.rect.Rect(0, 0, 0, 0)
        self.x = x
        self.y = y
        self.borderColor = 'black'
        self.backgroundColor = color
        self.alpha = 255
        self.lineWidth = 0
        self.screen = screen
        self.textValue = []

        if isSettings:
            for i, (label, mini, maxi, default, (handleColor, backgroundColor)) in enumerate(
                    Parameters.SLIDERS_DESCRIPTORS):
                self.addSlider(30, 50 + (i * 75), 200, 20, mini, maxi, default, handleColor, backgroundColor,
                               label, 'Aharoni', 20, self.display.get_width(), 50 + (i * 150),
                               'white')

    def addText(self, content, font, fontSize, width, height, color):
        self.texts.append(displayText(content, font, fontSize, width, height, color))
        return len(self.texts) - 1

    def addSlider(self, x, y, widthSlider, heightSlider, mini, maxi, initial, handleColor, color,
                  label, font, fontSize, widthLabel, heightLabel, colorLabel):
        self.sliders.append(Slider(self.display, x, y, widthSlider, heightSlider, min=mini, max=maxi, initial=initial,
                                   handleColour=handleColor, colour=color))
        self.labels.append(displayText(label, font, fontSize, widthLabel, heightLabel, colorLabel))
        self.textValue.append(self.addText(str(self.sliders[-1].getValue()), font, fontSize, self.display.get_width() * 1.8, y*2.15, color))

    def addRect(self, color, x, y, width, height, lineWidth):
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.borderColor = color
        self.lineWidth = lineWidth

    def setText(self, index, value, font='Aharoni', fontSize=20, color='white'):
        font = pygame.font.SysFont(font, fontSize)
        text = font.render(value, True, color)
        self.texts[index][0] = text

    def update(self, events):
        self.display.fill(self.backgroundColor)
        pygame_widgets.update(events)
        for value, slider in zip(self.textValue, self.sliders):
            self.setText(value, str(slider.getValue()))

        for text in self.texts:
            self.display.blit(text[0], text[1])

        for label in self.labels:
            self.display.blit(label[0], label[1])

        pygame.draw.rect(self.display, self.borderColor, self.rect, self.lineWidth)

    def render(self, events):
        self.update(events)
        self.display.set_alpha(self.alpha)
        self.screen.blit(self.display, (self.x, self.y))

    def __getitem__(self, item):
        """
        Use menuInstance.[Parameters.<DESIRED_PARAMETER>] helper to get the value of the slider
        :param int item:
        :return:
        """
        return self.sliders[item].value


class Parameters:
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    SLIDERS_DESCRIPTORS: List[
        Tuple[
            str, int, int, int,
            Tuple[
                Tuple[int, int, int], Tuple[int, int, int]
            ]
        ]
    ] = [
        ('Nombre de particules', 1, 20, 8, (red, white)),
        ('Vitesse de tir', 1, 10, 3, (green, white)),
        ('Vent', -10, 10, 0, (blue, white))
    ]

    NUMBER_PARTICLES = 0
    SHOOTING_SPEED = 1
    WIND = 2
