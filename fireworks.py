# Modules nécessaires
import pygame, math
from physicalObject import PhysicalObject
from movement import definedTrajectoryMovement, movementEquation


class Particle(PhysicalObject):
    '''
    Classe créant une particule se déplaçant avec une équation de mouvement.
    
    S'initialise lors de la création d'un feu d'artifice.
    '''
    def __init__(self, x, y, screen, speedX, speedY, size) -> None:
        '''
        Initialisation d'une instance Particle
        :arg x, float, coordonnée x de la position de la particule
        :arg y, float, coordonnée y de la position de la particule
        '''
        size = 10
        super().__init__(screen, x, y, speedX*2, speedY*3, 0, 5)
    
    def render(self):
        pygame.draw.circle(self.screen, "red", (self.x, self.y), self.size)

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
            self.particles.append(Particle(x, y, self .screen, math.sin(math.radians(i*(360/8))), math.cos(math.radians(i*(360/8)))))

    def update(self):
        '''Met à jour les particules'''
        for particle in self.particles:
            particle.render()

    def updateParticleMovement(self, dt):
        for particle in self.particles:
            definedTrajectoryMovement(particle, movementEquation(particle, dt))
