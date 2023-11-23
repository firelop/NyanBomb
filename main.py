from fireworks import Firework
from turret import Turret
from flower import Flower
import pygame, math, random, time

pygame.init()
monitorInfo = pygame.display.Info()  # Get the resolution of the screen
screen = pygame.display.set_mode((monitorInfo.current_w * .9, monitorInfo.current_h * .9))
pygame.display.set_caption("NyanBomb")  # Set the window title
clock = pygame.time.Clock()
running = True
fireworks = []
dt = 0
turret = Turret(screen)
isHoldingClick = False
size = 5
x, y = 0, 0
allParticles = []
colliding = 0
flowers = []
closestParticle = None

def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 1,0 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 0,1 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )     

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill( (0, 0, 0) )
    gradientRect(screen, (13, 119, 212), (33, 133, 126), pygame.Rect(0, 0, monitorInfo.current_w * .9, monitorInfo.current_h * .9))
    pygame.draw.rect(screen, (54, 33, 25), pygame.Rect(0, monitorInfo.current_h*.9-30, monitorInfo.current_w*.9, 30))
    dt = clock.tick(120) / 1000  # Represent the time spent since the last frame

    if pygame.mouse.get_pressed()[0]:
        if not isHoldingClick:
            x, y = pygame.mouse.get_pos()
            isHoldingClick = True
        else:
            if size < 100:
                size += 50 * dt
            pygame.draw.circle(screen, 'white', (x, y), size)

    elif isHoldingClick:
        isHoldingClick = False
        newFirework = Firework(x, y, screen, size, dt)
        fireworks.append(newFirework)
        for particle in newFirework.particles:
            allParticles.append(particle)
        size = 5

    for firework in fireworks:
        firework.updateParticleMovement(dt)
        firework.update(dt)

    if (len(fireworks) != 0) and ((time.time() - 0.3) > turret.lastShootedAt):
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

    pygame.display.flip()

pygame.quit()
