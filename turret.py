import pygame, math, time


class Turret:
    def __init__(self, screen):
        # Place at the bottom right
        self.windowSize = pygame.display.get_window_size()
        # self.x = self.windowSize[0]
        # self.y = self.windowSize[1]
        self.size = 50
        self.x = self.windowSize[0]-self.size
        self.y = self.windowSize[1]-self.size-10
        self.screen = screen
        self.rotation = 0
        self.color = (8, 82, 12)
        self.lasers = []
        self.lastShootedAt = time.time()

    def render(self):
        
        for ball in self.lasers:
            ball.render()
            if ball.x < 0 or ball.x > self.windowSize[0] or ball.y < 0 or ball.y > self.windowSize[1]:
                self.lasers.remove(ball)

        pygame.draw.circle(self.screen, self.color, (self.x - self.size, self.y), 50)
        head = pygame.Surface((self.size * 4, self.size * 4), pygame.SRCALPHA)
        head.fill((0, 0, 0, 0))
        pygame.draw.rect(head, self.color, (self.size * 1.75, 0, self.size // 2, self.size))
        head = pygame.transform.rotate(head, self.rotation)
        headRect = head.get_rect()
        headRect.center = (self.x - self.size, self.y)

        pygame.draw.rect(self.screen, self.color, (self.x-self.size*2, self.y+self.size/2+10, 100, 25))

        self.screen.blit(head, headRect)

    def shootAt(self, x, y):
        """
        Make the turret shoot a certain point
        :arg x int The x position of the point to shoot at
        :arg y int The y position of the point to shoot at
        :return void
        """
        relativeX = x - self.x
        relativeY = y - self.y
        self.rotation = ((180 / 3.1415) * - math.atan2(relativeY, relativeX)) - 90
        self.lasers.append(Laser(self.screen, self.x - self.size, self.y, self.rotation))
        self.lastShootedAt = time.time()


class Laser:
    def __init__(self, screen, x, y, direction):
        self.screen = screen
        self.speed = 100
        self.xOrigin = x
        self.yOrigin = y
        self.x = x
        self.y = y
        self.size = 10
        self.color = (255, 25, 50)
        self.direction = (-math.radians(direction + 90))

    def render(self):
        x = self.x + math.cos(self.direction) * self.speed
        y = self.y + math.sin(self.direction) * self.speed
        pygame.draw.line(self.screen, self.color, (self.xOrigin, self.yOrigin), (int(x), int(y)), self.size)
        self.x = x
        self.y = y
