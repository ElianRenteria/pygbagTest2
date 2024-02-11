import random
import pygame

class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 50
        self.left = pygame.Rect(self.x, self.y, 10, 50)
        self.right = pygame.Rect(self.x+290, self.y, 10, 50)
        self.top = pygame.Rect(self.x+10, self.y, 280, 10)
        self.bottom = pygame.Rect(self.x+10, self.y+40, 280, 10)
        self.image = pygame.transform.scale(pygame.image.load("branch.png"), (300,160))
    def draw(self, window):
        window.blit(self.image, (self.x, self.y-55))
        #pygame.draw.rect(window, (0, 0, 255), self.top)
        #pygame.draw.rect(window, (0, 0, 0), self.bottom)
        #pygame.draw.rect(window, (255, 0, 0), self.left)
        #pygame.draw.rect(window, (0, 255, 0), self.right)