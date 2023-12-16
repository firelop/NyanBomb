from typing import List, Tuple

import pygame_widgets
from pygame_widgets.slider import Slider
import pygame


def displayText(content, font, fontSize, width, height, color):
    """
    Affiche du texte sur une surface avec la police, la taille, et la couleur spécifiées.

    :arg content, str, Le contenu du texte à afficher.
    :arg font, str, La police du texte.
    :arg fontSize, int, La taille de la police.
    :arg width, int, La largeur de la surface.
    :arg height, int, La hauteur de la surface.
    :arg color, Tuple[int, int, int] La couleur du texte en format RGB.
     
    :return Une liste contenant la surface du texte et son rectangle d'emplacement.
    :rtype: List[pygame.Surface, pygame.Rect]
    """
    font = pygame.font.SysFont(font, fontSize)
    text = font.render(content, True, color)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 2)
    return [text, textRect]


class Menu:
    """
    Initialise un menu avec une surface, des éléments graphiques et des fonctionnalités spécifiques.

    :arg screen, La surface sur laquelle le menu sera affiché.
    :arg x, int, La position en x du coin supérieur gauche du menu sur la surface d'affichage.
    :arg y, int, La position en y du coin supérieur gauche du menu sur la surface d'affichage.
    :arg size, Tuple[int, int] La taille du menu sous la forme d'un tuple (largeur, hauteur).
    :arg color, Tuple[int, int, int], La couleur de fond du menu en format RGB.
    :arg isSettings, bool, Indique si le menu est un menu de paramètres (contenant des sliders).

    :return: Aucune valeur de retour explicite.
    """
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
        """
        Ajoute un texte au menu.

        :arg content, str, Le contenu du texte à ajouter.
        :arg font, str, La police du texte.
        :arg fontSize, int, La taille de la police.
        :arg width, int, La largeur de la surface du menu.
        :arg height, int, La hauteur de la surface du menu.
        :arg color, Tuple[int, int, int], La couleur du texte en format RGB.

        :return: L'index du texte ajouté.
        :rtype: int
        """
        self.texts.append(displayText(content, font, fontSize, width, height, color))
        return len(self.texts) - 1

    def addSlider(self, x, y, widthSlider, heightSlider, mini, maxi, initial, handleColor, color,
                  label, font, fontSize, widthLabel, heightLabel, colorLabel):
        """
        Ajoute un slider au menu.

        :arg x, int, La position en x du coin supérieur gauche du slider.
        :arg y, int, La position en y du coin supérieur gauche du slider.
        :arg widthSlider, int, La largeur du slider.
        :arg heightSlider, int, La hauteur du slider.
        :arg mini, int, La valeur minimale du slider.
        :arg maxi, int, La valeur maximale du slider.
        :arg initial, int, La valeur initiale du slider.
        :arg handleColor, Tuple[int, int, int], La couleur du curseur du slider en format RGB.
        :arg color, Tuple[int, int, int], La couleur du slider en format RGB.
        :arg label, str, Le label associé au slider.
        :arg font, str, La police du texte du label du slider.
        :arg fontSize, int, La taille de la police du texte du label du slider.
        :arg widthLabel, int, La largeur de la surface du label du slider.
        :arg heightLabel, int, La hauteur de la surface du label du slider.
        :arg colorLabel, Tuple[int, int, int], La couleur du texte du label du slider en format RGB.

        :return None
        """
        self.sliders.append(Slider(self.display, x, y, widthSlider, heightSlider, min=mini, max=maxi, initial=initial,
                                   handleColour=handleColor, colour=color))
        self.labels.append(displayText(label, font, fontSize, widthLabel, heightLabel, colorLabel))
        self.textValue.append(self.addText(str(self.sliders[-1].getValue()), font, fontSize, self.display.get_width() * 1.8, y*2.15, color))

    def addRect(self, color, x, y, width, height, lineWidth):
        """
        Ajoute un rectangle au menu.

        :arg color, Tuple[int, int, int], La couleur du rectangle en format RGB.
        :arg x, int, La position en x du coin supérieur gauche du rectangle.
        :arg y, int, La position en y du coin supérieur gauche du rectangle.
        :arg width, int, La largeur du rectangle.
        :arg height, int, La hauteur du rectangle.
        :arg lineWidth, int, L'épaisseur de la ligne du rectangle.

        :return None
        """
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.borderColor = color
        self.lineWidth = lineWidth

    def setText(self, index, value, font='Aharoni', fontSize=20, color='white'):
        """
        Modifie le texte à l'index spécifié.

        :arg index, int, L'index du texte à modifier.
        :arg value, str, La nouvelle valeur du texte.
        :arg font, str, La police du texte.
        :arg fontSize, int, La taille de la police.
        :arg color, str, La couleur du texte en format RGB.

        :return None
        """
        font = pygame.font.SysFont(font, fontSize)
        text = font.render(value, True, color)
        self.texts[index][0] = text

    def update(self, events):
        """
        Met à jour le menu en fonction des événements.

        :arg events, List[pygame.event.Event], La liste des événements à prendre en compte.

        :return None
        """
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
        """
        Rend le menu à l'écran.

        :arg events, List[pygame.event.Event], La liste des événements à prendre en compte.

        :return None
        """
        self.update(events)
        self.display.set_alpha(self.alpha)
        self.screen.blit(self.display, (self.x, self.y))

    def __getitem__(self, item):
        """
        Utilisez menuInstance.[Parameters.<DESIRED_PARAMETER>] pour obtenir la valeur du slider.

        :arg item, int, L'index du slider.

        :return La valeur actuelle du slider.
        """
        return self.sliders[item].value


class Parameters:
    '''
    Classe gérant les paramètres du jeu.
    S'initialise au lancement du programme.
    '''
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
