import pygame
from pygame.locals import *

# Initialization
pygame.init()
WIDTH = 640
HEIGHT = 480
FPS = 60

# DEFINE COLOURS
BG = (3, 31, 64)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# INITIALIZE PYGAME AND CREATE WINDOW

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pong!")
clock = pygame.time.Clock()
title_font = pygame.font.SysFont("calibri", 60)
font = pygame.font.SysFont("calibri", 40)
sub_font = pygame.font.SysFont("calibri", 20)

back = pygame.Surface((WIDTH, HEIGHT))
background = back.convert()
background.fill(BG)

# Game loop

Main_Loop = True
while Main_Loop:

    # keep loop running or the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_1:
                from P1vsP2 import *
                Main_Loop = False
            elif event.key == K_2:
                from P1vsAi import *
                Main_Loop = False
        # check for closing windows
        if event.type == pygame.QUIT:
            Main_Loop = False

    # Title
    title = title_font.render(str('Ping Pong!'), True, YELLOW)
    P1vsP2 = font.render(str('P1vsP2'), True, WHITE)
    Press1 = sub_font.render(str('Press 1'), True, BLACK)
    P1vsAL = font.render(str('P1vsAL'), True, WHITE)
    Press2 = sub_font.render(str('Press 2'), True, BLACK)

    # draw / render
    screen.blit(background, (0, 0))
    screen.blit(title, (200., 150.))
    screen.blit(P1vsP2, (100., 300.))
    screen.blit(P1vsAL, (420., 300.))
    screen.blit(Press1, (130., 350.))
    screen.blit(Press2, (450., 350.))

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
