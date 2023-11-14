# Modules nécessaires
import pygame, math


class Particle:
    '''
    Classe créant une particule se déplaçant avec une équation de mouvement.
    
    S'initialise lors de la création d'un feu d'artifice.
    '''
    def __init__(self, x, y, screen, accelX, accelY=0) -> None:
        '''
        Initialisation d'une instance Particle
        :arg x, float, coordonnée x de la position de la particule
        :arg y, float, coordonnée y de la position de la particule
        '''
        self.accelX = accelX
        self.accelY = accelY
        self.x = x
        self.y = y
        self.screen = screen
    
    def render(self):
        self.x += self.accelX
        self.y += self.accelY
        pygame.draw.circle(self.screen, "red", (self.x, self.y), 10)

class Firework:
    '''
    Classe créant un feu d'artifice visible par le client.
    
    la classe s'initialise lors du clic par le client
    '''
    def __init__(self, x, y, screen) -> None:
        '''
        Initialisation d'une instance Firework
        :arg x, float, coordonnée x de la position de la particule
        :arg y, float, coordonnée y de la position de la particule
        '''
        particleAccelX = [2*j-j for j in range(8)]
        self.screen = screen
        self.particles = []
        for i in range(8):
            self.particles.append(Particle(x, y, self .screen, math.sin(math.radians(i*(360/8)))))

    def update(self):
        '''Met à jour les particules'''
        for particle in self.particles:
            particle.render()
