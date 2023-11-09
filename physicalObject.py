import pygame
class PhysicalObject:
    '''
    Classe représentant un objet et ses propriétés physiques
    '''
    def __init__(self, window):
        '''
        Constructeur de la classe PhysicalObject
        '''
        self.x = 'int or float'                 # Position x initiale de l'objet sur l'écran
        self.y = 'int or float'                 # Position y initiale de l'objet sur l'écran
        
        self.speedX = 'int or float'            # Vitesse initiale de l'objet sur l'axe x, si elle est positive, l'objet se dirigera INITIALEMENT vers la droite, sinon, il se dirigera vers la gauche
        self.speedY = 'int or float'            # Vitesse initiale de l'objet sur l'axe y, si elle est positive, l'objet se dirigera INITIALEMENT vers le bas, sinon, il se dirigera vers le haut
        
        self.accelerationX = 'int or float'     # Accélération initiale de l'objet sur l'axe x, si elle est positive, l'objet se dirigera vers la gauche, sinon, il se dirigera vers la droite
        self.accelerationY = 'int or float'     # Accélération initiale de l'objet sur l'axe x, si elle est positive, l'objet se dirigera vers le bas, sinon, il se dirigera vers la gauche
        
        self.window = window                    # Fenêtre sur laquelle l'objet s'affichera
        self.display = self.render()            # Appel de la fonction render pour que l'objet s'affiche à sa création
        
    def render(self):
        '''
        Fonction gérant l'affichage de l'objet sur l'écran
        '''
        self.display = 'function'               # Affichage de l'objet sur l'écran