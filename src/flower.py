import pygame, os, random, time

animation = [("corn", 20), ("eggplant", 9), ("watermelon", 19), ("wheat", 7), ("cucumber", 20), ("onion", 6),
             ("tomat", 20)]

frames = {
}

for flowerName, animationSize in animation:
    frames[flowerName] = []
    for i in range(1, animationSize+1):
        image = pygame.image.load(os.path.join("assets", flowerName, f"{flowerName}_{i}.png"))
        frames[flowerName].append(pygame.transform.scale(image, (int(image.get_width() * 3), int(image.get_height() * 3))))


class Flower:
    '''
    Classe créant une fleur au point de chute de particule de feu d'artifice et poussant au fil du temps, avant de disparaître.
    
    S'initialise lorsqu'une particule de feu d'artifice atteint le sol.
    '''
    def __init__(self, screen, x):
        '''
        Initialisation d'une instance Flower
        :arg x, float, coordonnée x de la position de la fleur
        :arg screen, surface sur laquelle la fleur s'affichera
        '''
        self.rect = None
        self.flowerName, self.animationSize = random.choice(animation)
        self.plantedAt = time.time()
        self.screen = screen

        self.y = screen.get_height() + random.randint(-5, 10)
        self.currentFrame = 0
        image = frames[self.flowerName][int(self.currentFrame)]
        self.x = x - image.get_width() / 2

    def render(self, dt):
        '''
        Gère l'affichage de la fleur.
        :arg dt, float, Temps écoulé depuis la dernière frame (en secondes).
        :return None
        '''
        if self.currentFrame < self.animationSize - 1:
            self.currentFrame += (10 * dt) / self.animationSize

        image = frames[self.flowerName][int(self.currentFrame)]
        self.rect = image.get_rect()
        self.screen.blit(image, (self.x, self.y - image.get_height() - 10))
