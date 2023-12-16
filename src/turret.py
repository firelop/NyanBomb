import pygame, math, time


class Turret:
    '''
    Classe créant une tourelle.
    
    S'initialise lorsque le jeu est lancé.
    '''
    def __init__(self, screen):
        """
        Initialise une instance de Turret.

        :arg screen, La surface d'affichage de la fenêtre du jeu.
        """
        # Place at the bottom right
        self.windowSize = pygame.display.get_window_size()
        # self.x = self.windowSize[0]
        # self.y = self.windowSize[1]
        self.size = 50
        self.x = self.windowSize[0]-self.size
        self.y = self.windowSize[1]-self.size
        self.screen = screen
        self.rotation = 0
        self.color = (8, 82, 12)
        self.lasers = []
        self.lastShootedAt = time.time()

    def render(self):
        """
        Rend la tourelle à l'écran.
        """
        for ball in self.lasers:
            ball.render()
            if ball.x < 0 or ball.x > self.windowSize[0] or ball.y < 0 or ball.y > self.windowSize[1]:
                self.lasers.remove(ball)

        pygame.draw.circle(self.screen, self.color, (self.x - self.size, self.y), 50)
        head = pygame.Surface((self.size * 4, self.size * 4), pygame.SRCALPHA)
        head.fill((0, 0, 0, 0))
        pygame.draw.rect(head, self.color, (self.size * 1.75, 0, self.size // 2, self.size))
        head = pygame.transform.rotate(head, self.rotation - 90)
        headRect = head.get_rect()
        headRect.center = (self.x - self.size, self.y)

        pygame.draw.rect(self.screen, self.color, (self.x-self.size*2, self.y+self.size/2+10, 100, 25))

        self.screen.blit(head, headRect)

    def shootAt(self, x, y):
        """
        Fait tirer la tourelle vers un point spécifique.

        :arg int x: La position en x du point à viser.
        :arg int y: La position en y du point à viser.
        :return None
        """
        relativeX = x - self.x + self.size
        relativeY = y - self.y
        self.rotation = ((180 / math.pi) * - math.atan2(relativeY, relativeX))
        self.lasers.append(Laser(self.screen, self.x - self.size, self.y, self.rotation))
        self.lastShootedAt = time.time()


class Laser:
    def __init__(self, screen, x, y, direction):
        """
        Initialise une instance de Laser.

        :arg screen, La surface d'affichage de la fenêtre du jeu.
        :arg x, int, La position en x du laser.
        :arg y, int, La position en y du laser.
        :arg direction, float, La direction du laser en radians.
        """
        self.screen = screen
        self.speed = 100
        self.xOrigin = x
        self.yOrigin = y
        self.x = x
        self.y = y
        self.size = 10
        self.color = (255, 25, 50)
        self.direction = (-math.radians(direction))

    def render(self):
        """
        Rend le laser à l'écran.
        """
        x = self.x + math.cos(self.direction) * self.speed
        y = self.y + math.sin(self.direction) * self.speed
        pygame.draw.line(self.screen, self.color, (self.xOrigin, self.yOrigin), (int(x), int(y)), self.size)
        self.x = x
        self.y = y
        self.xOrigin = self.xOrigin + math.cos(self.direction) * self.speed
        self.yOrigin = self.yOrigin + math.sin(self.direction) * self.speed
