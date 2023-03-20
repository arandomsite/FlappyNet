# modules
import os
import pygame
from pygame.locals import *
# pip install pygame

# Starting Window
if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")
    
screen = pygame.display.set_mode([128, 128])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Put all game code between here
    screen.fill((173, 216, 230))
    bg = pygame.image.load("assets/bg.png").convert()
    screen.blit(bg, (0, 0))
    pygame.display.set_caption("FlappyNet")
    player = Rect(10, 113, 10, 10)
    # Add player movements below here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.top -= 10;
    
    if keys[pygame.K_LEFT]:
        player.left -= 10;
    
    if keys[pygame.K_RIGHT]:
        player.left += 10;
    # and above herea
    pygame.draw.rect(screen, (0, 255, 0), player)
    # And here
    pygame.display.flip()

pygame.quit()