# Import external libraries
# Import internal (nyanbomb) libraries
from typing import List, Tuple

import math
import pygame
import random
import time

from fireworks import Firework, Particle
from flower import Flower
from menu import Menu, Parameters
from turret import Turret

FIREWORK_SPAWN_DELAY = 1
TURRET_SHOOT_DELAY = 0.7


def gradientRect(window, upColour, downColour, targetRect):
    """
    Draw a vertical-gradient filled rectangle covering <target_rect>

    :param pygame.Surface window:  The surface to draw the gradient on
    :param Tuple[int, int, int] upColour: The up RGB color
    :param Tuple[int, int, int] downColour: The down RGB color
    :param pygame.Rect targetRect: The rect the gradient will be resized to
    """
    colourRect = pygame.Surface((2, 2))  # tiny! 2x2 bitmap
    pygame.draw.line(colourRect, upColour, (0, 0), (1, 0))  # left colour line
    pygame.draw.line(colourRect, downColour, (0, 1), (1, 1))  # right colour line
    colourRect = pygame.transform.smoothscale(colourRect, (targetRect.width, targetRect.height))  # stretch!
    window.blit(colourRect, targetRect)


class Game:

    def __init__(self, screen, startMenu: Menu, settings: Menu):
        """
        Constructor from the Game class
        :param pygame.Surface screen: The surface to draw on
        """
        # Miscellanous
        self.isLaunched: bool = True
        self.monitorInfo: pygame.display.Info() = pygame.display.Info()

        # Setting surface up
        self.screen: pygame.Surface = screen

        # Setting up "sprites"
        self.fireworks: List[Firework] = []  # Handle all fireworks
        self.turret: Turret = Turret(self.screen)
        self.flowers: List[Flower] = []  # Handle all flowers
        self.allParticles: List[Particle] = []  # Used to iterate through all particles more easily

        # Time related variables
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.fireworkLastLaunchedAt: float = time.time()  # Used to delay the launch of fireworks
        self.turretLastShotAt: float = time.time()  # Used to delay the turret shots

        # Menu related variables
        self.startMenu: Menu = startMenu
        self.startMenuShown: bool = True
        self.settings: Menu = settings

    def clearDisplay(self):
        """
        Clears the display
        :return None
        """
        self.screen.fill((0, 0, 0))

    def checkLaserCollideParticles(self):
        for particle in self.allParticles:
            particleAngle = ((180 / math.pi) * -math.atan2(particle.y - self.turret.y, particle.x - self.turret.x))
            if self.turret.rotation < particleAngle < self.turret.rotation + particle.size:
                particle.destructedByTurret = True
                particle.isDestructed = True

    def update(self, dt):
        """
        Every update is made here (but the fireworks particles update that is made in the render)
        :param float dt: The time spent since the last frame generally called delta time
        :return None
        """
        mouseX, mouseY = pygame.mouse.get_pos()

        if mouseY < self.settings.display.get_height() and mouseX < self.settings.display.get_width():
            self.settings.alpha = 255
        else:
            self.settings.alpha = 127

            if pygame.mouse.get_pressed()[0] and time.time() - self.turretLastShotAt > 1/self.settings[Parameters.SHOOTING_SPEED]:
                self.turretLastShotAt = time.time()
                self.turret.shootAt(mouseX, mouseY)
                self.checkLaserCollideParticles()

        for firework in self.fireworks:
            firework.updateParticleMovement(dt)

        for flower in self.flowers:
            if (time.time() - flower.plantedAt) > 10:
                self.flowers.remove(flower)

    def render(self, dt, events):
        """
        Render all the "sprites" such as particles, turret, laser and flowers
        :param float dt: The time spent since the last frame generally called delta time
        :param List[pygame.event.Event] events: The events that happened since the last frame
        :return None
        """
        self.clearDisplay()
        gradientRect(self.screen, (0, 2, 36), (18, 22, 89),
                     pygame.Rect(0, 0, self.monitorInfo.current_w, self.monitorInfo.current_h))
        pygame.draw.rect(self.screen, (54, 33, 25),
                         pygame.Rect(0, self.screen.get_height() - 30, self.screen.get_width(), 30))

        for particle in self.allParticles:
            if particle.isDestructed:
                if not particle.destructedByTurret:
                    self.flowers.append(Flower(self.screen, particle.x))
                self.allParticles.remove(particle)
                continue
            particle.render()

        for flower in self.flowers:
            flower.render(dt)

        self.turret.render()
        self.settings.render(events)
        pygame.display.flip()  # Revert display buffers

    def spawnFirework(self):
        """
        Spawns a firework at a random place
        :return None
        """
        newFirework = Firework(
            random.randint(20, int(self.monitorInfo.current_w * .9) - 20),
            random.randint(20, int(self.monitorInfo.current_h * .3)),
            self.screen,
            random.randint(10, 30),
            (
                random.randint(100, 255),
                random.randint(100, 255),
                random.randint(100, 255)
            ),
            self.settings
        )
        self.fireworks.append(newFirework)
        # Adding all particles to the self.allParticles
        for particle in newFirework.particles:
            self.allParticles.append(particle)

        self.fireworkLastLaunchedAt = time.time()

    def play(self):
        """
        Main loop
        :return None
        """
        while self.isLaunched:
            # Handle events
            dt = self.clock.tick(60) / 1000
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.isLaunched = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.isLaunched = False
                    elif event.key == pygame.K_SPACE:
                        self.startMenuShown = False

            if time.time() - self.fireworkLastLaunchedAt > FIREWORK_SPAWN_DELAY:
                self.spawnFirework()

            if self.startMenuShown:
                self.startMenu.render(events)
                pygame.display.flip()
            else:
                self.update(dt)
                self.render(dt, events)
