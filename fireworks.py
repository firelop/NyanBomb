# Modules nécessaires
import pygame, math, random
from physicalObject import PhysicalObject
from movement import definedTrajectoryMovement, movementEquation


class Particle(PhysicalObject):
    '''
    Classe créant une particule se déplaçant avec une équation de mouvement.
    
    S'initialise lors de la création d'un feu d'artifice.
    '''
    def __init__(self, x, y, screen, speedX, speedY, size, firework, dt, color) -> None:
        '''
        Initialisation d'une instance Particle
        :arg x, float, coordonnée x de la position de la particule
        :arg y, float, coordonnée y de la position de la particule
        '''
        self.size = size
        self.coef = self.size/5
        self.colorChange = 30 + random.randint(0, 10)
        self.isRendered = True
        self.color = color
        self.collindingList = []
        self.isDestructed = False
        self.destructedByTurret = False
        self.firework = firework
        super().__init__(screen, x, y, speedX*self.coef, speedY*self.coef, 0, 2*self.coef, dt)
    
    def render(self):
        self.colorChange -= 1
        if self.isRendered:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size) 
            
        if self.colorChange == 0:
            self.colorChange = 20
            self.isRendered = not self.isRendered

    def collide(self, otherParticle):
        particleToDestroy = self if self.size < otherParticle.size else otherParticle
        particleToKeep = otherParticle if self.size < otherParticle.size else self
        if particleToDestroy in particleToDestroy.firework.particles:
            particleToDestroy.firework.particles.remove(particleToDestroy)
        particleToDestroy.isDestructed = True
        particleToKeep.size += particleToDestroy.size/2
        particleToKeep.color = ((particleToKeep.color[0] + particleToDestroy.color[0])/2, (particleToKeep.color[1] + particleToDestroy.color[1])/2, (particleToKeep.color[2] + particleToDestroy.color[2])/2)






class Firework:
    '''
    Classe créant un feu d'artifice visible par le client.
    
    la classe s'initialise lors du clic par le client
    '''
    def __init__(self, x, y, screen, size, dt, color) -> None:
        '''
        Initialisation d'une instance Firework
        :arg x, float, coordonnée x de la position de la particule
        :arg y, float, coordonnée y de la position de la particule
        '''
        self.screen = screen
        self.size = size
        self.numberOfParticles = 8
        self.particles = []
        self.color = color
        for i in range(self.numberOfParticles):
            self.particles.append(
                Particle(
                    x, y,
                    self.screen,
                    math.sin(math.radians(i*(360/self.numberOfParticles))) + random.random()/4 - .125,
                    math.cos(math.radians(i*(360/self.numberOfParticles))) + random.random()/4 - .125,
                    self.size,
                    self,
                    dt,
                    self.color
                )
            )

    def update(self, dt):
        '''Met à jour les particules'''
        for particle in self.particles:
            if particle.isDestructed:
                self.particles.remove(particle)
            particle.render()

    def updateParticleMovement(self, dt):
        for particle in self.particles:
            definedTrajectoryMovement(particle, movementEquation(particle, dt))
            if (particle.y > self.screen.get_height()) or (particle.x < 0) or (particle.x > self.screen.get_width()):
                particle.isDestructed = True
                self.particles.remove(particle)

        if len(self.particles) == 0:
            del self

