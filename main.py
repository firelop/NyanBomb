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
color = (0, 0, 0)
fireworkTimer = 0
lastFirework = 2

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
            
    fireworkTimer = time.time()
    
    if (fireworkTimer - lastFirework) > 3 :
        newFirework = Firework(random.randint(20, int(monitorInfo.current_w*.9)-20), random.randint(20, int(monitorInfo.current_h*.45)), screen, random.randint(10, 30), dt, (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        fireworks.append(newFirework)
        for particle in newFirework.particles:
            allParticles.append(particle)
        lastFirework = time.time()

    screen.fill( (0, 0, 0) )
    gradientRect(screen, (0, 2, 36), (18, 22, 89), pygame.Rect(0, 0, monitorInfo.current_w * .9, monitorInfo.current_h * .9))
    pygame.draw.rect(screen, (54, 33, 25), pygame.Rect(0, monitorInfo.current_h*.9-30, monitorInfo.current_w*.9, 30))
    dt = clock.tick(120) / 1000  # Represent the time spent since the last frame

    if pygame.mouse.get_pressed()[0]:
        if not isHoldingClick:
            x, y = pygame.mouse.get_pos()
            isHoldingClick = True              
            turret.shootAt(x, y)
            if (turret.lastShootedAt - 0.3) > 0:
                for particle in allParticles:
                    particle_angle = ((180 / math.pi) * -math.atan2(particle.y - turret.y, particle.x - turret.x))
                    print(particle_angle, turret.rotation, particle.size)
                    if turret.rotation < particle_angle < turret.rotation + particle.size:
                        particle.destructedByTurret = True
                        particle.isDestructed = True
                        

        elif isHoldingClick:
            isHoldingClick = False

    for firework in fireworks:
        firework.updateParticleMovement(dt)
        firework.update(dt)

    for particle in allParticles:
        if particle.isDestructed:
            if not particle.destructedByTurret:
                flowers.append(Flower(screen, particle.x, particle.size / 10))
            allParticles.remove(particle)
            continue
        
        for otherParticle in allParticles:
            if particle.firework != otherParticle.firework:
                if math.sqrt((particle.x - otherParticle.x) ** 2 + (particle.y - otherParticle.y) ** 2) < particle.size / 2 + otherParticle.size / 2:
                    if particle not in otherParticle.collindingList and otherParticle not in particle.collindingList:
                        particle.collide(otherParticle)
                        particle.collindingList.append(otherParticle)
                        otherParticle.collindingList.append(particle)
                else:
                    if otherParticle in particle.collindingList:
                        particle.collindingList.remove(otherParticle)
                        otherParticle.collindingList.remove(particle)

    for flower in flowers:
        if (flower.life - flower.plantedAt) < 20:
            flower.render(dt)
        else:
            flowers.remove(flower)

    turret.render()

    pygame.display.flip()

pygame.quit()
