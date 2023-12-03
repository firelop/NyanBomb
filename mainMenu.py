from pygame_widgets.slider import Slider
from menuText import displayText
from fireworks import Firework
from turret import Turret
from flower import Flower
import pygame, math, random, time, pygame_widgets

pygame.init()
monitorInfo = pygame.display.Info()  # Get the resolution of the screen
screen = pygame.display.set_mode((monitorInfo.current_w * .9, monitorInfo.current_h * .9))
pygame.display.set_caption("NyanBomb")  # Set the window title
clock = pygame.time.Clock()
menu = True
play = False
fireworks = []
dt = 0
accueil, accueilRect = displayText('NyanBomb', 'comicsansms', 120, 0, 0, screen.get_width(), screen.get_height(), 'white')
jeu, jeuRect = displayText('Playing...', 'comicsansms', 0, 0, 50, 200, 50, 'white')
turret = Turret(screen)
isHoldingClick = False
size = 5
x, y = 0, 0
allParticles = []
colliding = 0
flowers = []
closestParticle = None

# Liste des paramètres à implémenter :
#   nbParticules, Vitesse de tir Tourelle
sliders = {}
parameters = ['Nombre de particules', 'Vitesse de tir']
handleColour = [(100, 100, 100), (50, 100, 50)]
colourParams = [(200, 200, 200), (100, 200, 100)]
minParams = [1, 3]
maxParams = [20, 10]
initParams = [8, 3]
posX, posY = 50, 100
sliderMenu = pygame.Surface((260, 60*len(parameters)))
i = 0
for parameter in parameters:
    sliders[parameter] = Slider(sliderMenu, 30, 20*((i+1)*2), 200, 20, min=minParams[i], max=maxParams[i], 
                                initial=initParams[i], handleColour=handleColour[i], colour=colourParams[i])
    i += 1

def game(screen, dt, menu, play, isHoldingClick, size, fireworks, allParticles, turret, flowers, x, y, closestParticle, nbParticles, shootSpeed):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT:
                play = False
                isHoldingClick = False
                size = 5
                allParticles = []
                flowers = []
    events = pygame.event.get()

    x, y = pygame.mouse.get_pos()

    screen.fill('black')

    screen.blit(jeu, jeuRect)
    screen.blit(sliderMenu, (posX, posY))
    
    if pygame.mouse.get_pressed()[0]:
        if not isHoldingClick and not(posX-20 <= x <= posX+270 and posY-20 <= y <= posY*len(parameters)+20):
            isHoldingClick = True
        elif not(posX-20 <= x <= posX+270 and posY-20 <= y <= posY*len(parameters)+20):
            if size < 100:
                size += 50 * dt
            pygame.draw.circle(screen, "white", (x, y), size)

    elif isHoldingClick and not(posX-20 <= x <= posX+270 and posY-20 <= y <= posY*len(parameters)+20):
        isHoldingClick = False
        newFirework = Firework(x, y, screen, size, dt, nbParticles)
        fireworks.append(newFirework)
        for particle in newFirework.particles:
            allParticles.append(particle)
        size = 5

    for firework in fireworks:
        firework.updateParticleMovement(dt)
        firework.update(dt)

    if (len(fireworks) != 0) and ((time.time() - (1/shootSpeed)) > turret.lastShootedAt):
        closestParticlePos = [0, 0]

        for firework in fireworks:
            if len(firework.particles) == 0:
                fireworks.remove(firework)
            for particle in firework.particles:
                if (particle.x > closestParticlePos[0]) and (particle.y > closestParticlePos[1]):
                    closestParticlePos[0] = particle.x
                    closestParticlePos[1] = particle.y
                    closestParticle = particle
        hit = random.randint(0, 8)
        if hit != 0:
            turret.shootAt(closestParticlePos[0] - 2, closestParticlePos[1] - 2)
            closestParticle.isDestructed = True
            closestParticle.destructedByTurret = True
        else:
            turret.shootAt(closestParticlePos[0] - 20, closestParticlePos[1] - 20)

    for particle in allParticles:
        if particle.isDestructed:
            if not particle.destructedByTurret:
                flowers.append(Flower(screen, particle.x, particle.size / 10))
                if len(flowers) > 50:  # Garde seulement les 10 dernières fleurs
                    flowers = flowers[-50:]
            allParticles.remove(particle)
            continue
        for otherParticle in allParticles:
            if particle.firework != otherParticle.firework:
                if math.sqrt((particle.x - otherParticle.x) ** 2 + (
                        particle.y - otherParticle.y) ** 2) < particle.size / 2 + otherParticle.size / 2:
                    if particle not in otherParticle.collindingList and otherParticle not in particle.collindingList:
                        particle.collide(otherParticle)
                        particle.collindingList.append(otherParticle)
                        otherParticle.collindingList.append(particle)
                else:
                    if otherParticle in particle.collindingList:
                        particle.collindingList.remove(otherParticle)
                        otherParticle.collindingList.remove(particle)

    for flower in flowers:
        flower.render()

    turret.render()

    pygame_widgets.update(events)
    pygame.display.flip()
    clock.tick(120)

    return menu, play, isHoldingClick, size, fireworks, allParticles, turret, flowers, x, y, closestParticle

while menu:
    if play:
        menu, play, isHoldingClick, size, fireworks, allParticles, turret, flowers, x, y, closestParticle,  = game(
            screen, dt, menu, play, isHoldingClick, size, fireworks, allParticles, turret, flowers, x, y, 
            closestParticle, sliders[parameters[0]].getValue(), sliders[parameters[1]].getValue())
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = True
            elif event.key == pygame.K_ESCAPE:
                menu = False
                play = False

    screen.fill('black')
    dt = clock.tick(120) / 1000  # Represent the time spent since the last frame
    screen.blit(accueil, accueilRect)

    pygame.display.flip()

pygame.quit()
