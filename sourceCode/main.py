import pygame
import asyncio
from Player import *
from branch import *

bg = pygame.transform.scale(pygame.image.load("background.png"),(1000, 700))

def draw(window, player, platforms):
    window.blit(bg,(0,0))
    player.draw(window, platforms)


async def main():
    window = pygame.display.set_mode((1000,700))
    player = Player()
    platforms = []
    platforms.append(Platform(550, 100))
    platforms.append(Platform(150, 200))
    platforms.append(Platform(300, 300))
    platforms.append(Platform(650, 400))
    platforms.append(Platform(400, 500))
    run = True
    framerate = pygame.time.Clock()
    while run:
        framerate.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw(window, player, platforms)
        for platform in platforms:
            platform.draw(window)
        pygame.display.update()
        await asyncio.sleep(0)



asyncio.run(main())

