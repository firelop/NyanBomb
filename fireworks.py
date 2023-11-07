# Modules nécessaires
import pygame

class Particle:
    '''
    Classe créant une particule se déplaçant avec une équation de mouvement.
    
    S'initialise lors de la création d'un feu d'artifice.
    '''
    def __init__(self, x, y) -> None:
        '''
        Initialisation d'une instance Particle
        :arg x, float, coordonnée x de la position de la particule
        :arg y, float, coordonnée y de la position de la particule
        '''
        self.x = x
        self.y = y
        self.display()
    
    def display(self, screen):
        pass

    def update(self):
        pass

class Firework:
    '''
    Classe créant un feu d'artifice visible par le client.
    
    la classe s'initialise lors du clic par le client
    '''
    def __init__(self, x, y) -> None:
        '''
        Initialisation d'une instance Firework
        :arg x, float, coordonnée x de la position de la particule
        :arg y, float, coordonnée y de la position de la particule
        '''
        self.particles = []
        for i in range(8):
            self.particles.append(Particle(x, y))
    
    def update(self):
        '''Met à jour les particules'''
        for particle in self.particles:
            particle.update()
