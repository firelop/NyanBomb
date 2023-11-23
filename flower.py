import pygame, os, random, time


class Flower(pygame.sprite.Sprite):
    def __init__(self, screen, x, scale):
        scale = 5 if scale > 5 else scale
        scale += 1
        self.flowerName, self.animationSize = random.choice(
            [("corn", 20), ("eggplant", 9), ("watermelon", 19), ("wheat", 7), ("cucumber", 20), ("onion", 6),
             ("tomat", 20)])
        self.plantedAt = time.time()
        self.screen = screen

        self.y = screen.get_height() + random.randint(-5, 10) 
        self.currentFrame = 0
        self.frames = [
            pygame.image.load(os.path.join("assets", self.flowerName, self.flowerName + "_" + str(i) + ".png"))
            for i in range(1, self.animationSize + 1)
        ]

        for i, frame in enumerate(self.frames):
            self.frames[i] = pygame.transform.scale(frame,
                                                    (int(frame.get_width() * scale), int(frame.get_height() * scale)))

        self.image = self.frames[self.currentFrame]
        self.x = x - self.image.get_width() / 2


    def render(self):
        if self.currentFrame < self.animationSize - 1:
            self.currentFrame += 0.1
            self.image = self.frames[int(self.currentFrame)]

        self.rect = self.image.get_rect()
        self.screen.blit(self.image, (self.x, self.y - self.image.get_height() - 10))
