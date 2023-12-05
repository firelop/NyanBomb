import pygame, pygame_widgets, time, random, math
from menu import displayText
from fireworks import Firework
from flower import Flower

def playing(screen, game, infos, clock, dt, menu, play, isHoldingClick, size, fireworks, allParticles, turret, flowers, x, y, closestParticle, nbParticles, shootSpeed, wind, counting):
    
    events = pygame.event.get()
    for event in events:
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

    screen.blit(game.display, (game.x, game.y))
    screen.blit(infos.display, (infos.x, infos.y))
    game.update('black')
    infos.update('black')

    pygame_widgets.update(events)

    x, y = pygame.mouse.get_pos()
    if x <= infos.display.get_width()+10 and y <= infos.display.get_height()+10:
        infos.display.set_alpha(255)
    else:
        infos.display.set_alpha(100)

    if pygame.mouse.get_pressed()[0] and not (x <= infos.display.get_width()+10 and y <= infos.display.get_height()+10):
        if not isHoldingClick:
            isHoldingClick = True
        else:
            if size < 100:
                size += 50 * dt
            pygame.draw.circle(game.display, "white", (x, y), size)

    elif isHoldingClick and not (x <= infos.display.get_width()+10 and y <= infos.display.get_height()+10):
        isHoldingClick = False
        newFirework = Firework(x, y, game.display, size, dt, nbParticles, wind)
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
                counting += 100
                game.texts[1] = displayText(str(counting), 'comicsansms', 60, game.display.get_width()*2-200, 180, 'white')
                flowers.append(Flower(game.display, particle.x, particle.size / 10))
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
    clock.tick(120)

    return menu, play, isHoldingClick, size, fireworks, allParticles, turret, flowers, x, y, closestParticle, counting