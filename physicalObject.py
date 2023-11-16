import pygame
class PhysicalObject:
    '''
    Classe représentant un objet et ses propriétés physiques
    '''
    def __init__(self, screen, x, y, speedX, speedY, accelerationX, accelerationY, dt):
        '''
        Constructeur de la classe PhysicalObject
        '''
        self.x = x                 # Position x initiale de l'objet sur l'écran
        self.y = y                 # Position y initiale de l'objet sur l'écran

        self.previousX = x         # Position x précédente de l'objet sur l'écran
        self.previousY = y         # Position y précédente de l'objet sur l'écran
        
        self.speedX = speedX            # Vitesse initiale de l'objet sur l'axe x, si elle est positive, l'objet se dirigera INITIALEMENT vers la droite, sinon, il se dirigera vers la gauche
        self.speedY = speedY            # Vitesse initiale de l'objet sur l'axe y, si elle est positive, l'objet se dirigera INITIALEMENT vers le bas, sinon, il se dirigera vers le haut
        
        self.accelerationX = accelerationX     # Accélération initiale de l'objet sur l'axe x, si elle est positive, l'objet se dirigera vers la gauche, sinon, il se dirigera vers la droite
        self.accelerationY = accelerationY     # Accélération initiale de l'objet sur l'axe x, si elle est positive, l'objet se dirigera vers le bas, sinon, il se dirigera vers la gauche
        
        self.screen = screen                    # Fenêtre sur laquelle l'objet s'affichera
        self.display = self.render(dt)            # Appel de la fonction render pour que l'objet s'affiche à sa création
        
    def render(self):
        '''
        Fonction gérant l'affichage de l'objet sur l'écran
        '''
        self.display = 'function'               # Affichage de l'objet sur l'écran