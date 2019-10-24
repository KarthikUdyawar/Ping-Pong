import pygame
from pygame.locals import *

# Initialization
pygame.init()
WIDTH = 640
HEIGHT = 480
FPS = 60

BAR_W = 10
BAR_H = 80
CIR_R = 15

# DEFINE COLOURS
BG = (3, 31, 64)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# some definitions
bar1_x, bar2_x = 10., 620.
bar1_y, bar2_y = 215., 215.
circle_x, circle_y = 307, 232
bar1_move, bar2_move = 0., 0.
speed_x, speed_y = 250., 250.
bar1_score, bar2_score = 0, 0
bar2_speed = 6
bar1_speed = 8
bar1_speed_L1 = 6
bar1_speed_L2 = 7
bar1_speed_L3 = 7.5
bar1_speed_M = 8
bar1_speed_H1 = 8.5
bar1_speed_H2 = 9
bar1_speed_H3 = 10
alpha = 1.03

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Ping Pong!")

# Creating 2 bars, a ball and background.
back = pygame.Surface((WIDTH, HEIGHT))
background = back.convert()
background.fill(BG)
bar = pygame.Surface((BAR_W, BAR_H))
bar1 = bar.convert()
bar1.fill(RED)
bar2 = bar.convert()
bar2.fill(BLUE)
circ_sur = pygame.Surface((CIR_R, CIR_R))
circ = pygame.draw.circle(circ_sur, GREEN, (CIR_R // 2, CIR_R // 2), CIR_R // 2)
circle = circ_sur.convert()
circle.set_colorkey(BLACK)

# clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 40)

# game loop
P1vsAL = True
while P1vsAL:

    # movement of circle
    time_passed = clock.tick(FPS)
    time_sec = time_passed / 1000.0

    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec

    for event in pygame.event.get():
        # quit
        if event.type == QUIT:
            P1vsAL = False

        # player control
        if event.type == KEYDOWN:
            if event.key == K_UP:
                bar2_move = -bar2_speed
            elif event.key == K_DOWN:
                bar2_move = bar2_speed
        elif event.type == KEYUP:
            if event.key == K_UP:
                bar2_move = 0.
            elif event.key == K_DOWN:
                bar2_move = 0.

    # Difficulty level
    if bar2_score >= bar1_score + 3:
        bar1_speed = bar1_speed_H3
    elif bar2_score == bar1_score + 2:
        bar1_speed = bar1_speed_H2
    elif bar2_score == bar1_score + 1:
        bar1_speed = bar1_speed_H1
    elif bar2_score == bar1_score - 1:
        bar1_speed = bar1_speed_L3
    elif bar2_score == bar1_score - 2:
        bar1_speed = bar1_speed_L2
    elif bar2_score <= bar1_score - 3:
        bar1_speed = bar1_speed_L1
    else:
        bar1_speed = bar1_speed_M

    # ai control
    if circle_x > WIDTH/2:
        if bar1_y < HEIGHT/2 - 40:
            bar1_move = bar1_speed
        elif bar1_y > HEIGHT/2 - 40:
            bar1_move = -bar1_speed
        else:
            bar1_move = 0
    else:
        if circle_y > bar1_y + 40:
            bar1_move = bar1_speed
        elif circle_y < bar1_y + 40:
            bar1_move = -bar1_speed
        else:
            bar1_move = 0

    # score
    score1 = font.render(str(bar1_score), True, WHITE)
    score2 = font.render(str(bar2_score), True, WHITE)

    # draw
    screen.blit(background, (0, 0))
    frame = pygame.draw.rect(screen, WHITE, Rect((5, 5), (630, 470)), 2)
    middle_line = pygame.draw.aaline(screen, WHITE, (330, 5), (330, 475))
    screen.blit(bar1, (bar1_x, bar1_y))
    screen.blit(bar2, (bar2_x, bar2_y))
    screen.blit(circle, (circle_x, circle_y))
    screen.blit(score1, (250., 210.))
    screen.blit(score2, (380., 210.))

    # motion
    bar1_y += bar1_move
    bar2_y += bar2_move

    # coalition between bars and ball
    if circle_x <= bar1_x + 10. and circle_y >= bar1_y - 7.5:
        if circle_y <= bar1_y + 72.5:
            circle_x = 20.
            speed_x = - (speed_x * alpha)
    if circle_x >= bar2_x - 15. and circle_y >= bar2_y - 7.5:
        if circle_y <= bar2_y + 72.5:
            circle_x = 605.
            speed_x = - (speed_x * alpha)

    # coalition between ball and edge / ball respond / score counter
    if circle_x < 5.:
        bar2_score += 1
        circle_x, circle_y = 320., 232.5
        bar1_y, bar_2_y = 215., 215.
        speed_x = 250
        speed_y = 250
    elif circle_x > 620.:
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
        speed_x = 250
        speed_y = 250

    # coalition between ball and side wall
    if circle_y <= 10.:
        speed_y = - (speed_y * alpha)
    elif circle_y >= 457.5:
        speed_y = - (speed_y * alpha)

    # coalition between bars and side wall
    if bar1_y <= 7:
        bar1_y = 7
    elif bar1_y >= 394:
        bar1_y = 394
    if bar2_y <= 7:
        bar2_y = 7
    elif bar2_y >= 394:
        bar2_y = 394

    # score and results
    if bar2_score >= 11 and bar2_score > bar1_score + 2:
        print("Blue Player Wins")
        P1vsAL = False

    if bar1_score >= 11 and bar1_score > bar2_score + 2:
        print("Red Player Wins")
        P1vsAL = False

    # update
    pygame.display.update()

pygame.register_quit(P1vsAL)
