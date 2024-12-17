import pygame
from Ball import Ball
from Paddle import Paddle

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

ball=Ball(pygame=pygame, x=300, y=300, xspeed=3, yspeed=3)
left_pad = Paddle(pygame=pygame, x=100, y=250)

running = True
while running:
    screen.fill((0, 0, 0))

    ball.move()
    ball.check_collision(left_pad)
    ball.draw(screen)
    left_pad.draw(screen)

    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
