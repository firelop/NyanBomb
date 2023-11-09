import pygame
import movement

pygame.init()
monitorInfo = pygame.display.Info()  # Get the resolution of the screen
screen = pygame.display.set_mode((monitorInfo.current_w*.93, monitorInfo.current_h*.93))
pygame.display.set_caption("NyanBomb")  # Set the window title
clock = pygame.time.Clock()
running = True
dt = 0

class Boule:
    
    def __init__(self, window) -> None:
        self.x = (monitorInfo.current_w*.93)/2-50
        self.y = (monitorInfo.current_h*.93)/2-50
        self.window = window
        self.speedX = -5
        self.speedY = -5
        self.display = self.render()
        self.accelerationX = 1
        self.accelerationY = 9.81
        
    def render(self):
        self.window.fill("black")
        self.display = pygame.draw.rect(self.window, "red", (self.x, self.y, 50, 50))
              
boule1 = Boule(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        
        
    movement.definedTrajectoryMovement(boule1, movement.movementEquation(boule1, dt))
    boule1.render()
    
    dt = clock.tick(60) / 1000  # Represent the time spent since the last frame
    
    pygame.display.flip()

pygame.quit()
