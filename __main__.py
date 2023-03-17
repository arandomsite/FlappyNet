# modules
import os
import pygame

# Starting Window
if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")
    
screen = pygame.display.set_mode([300, 300])

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
    pygame.display.flip()
    # And here

pygame.quit()