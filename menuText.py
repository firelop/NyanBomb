import pygame

def displayText(content, font, fontSize, rectangleSizeStartX, rectangleSizeStartY, rectangleSizeEndX, rectangleSizeEndY, color):
    font = pygame.font.Font(None, fontSize)
    text = font.render(content, False, color)
    textRect = text.get_rect()
    textRect.center = ((rectangleSizeEndX-rectangleSizeStartX)//2, (rectangleSizeEndY-rectangleSizeStartY)//2)
    return text, textRect