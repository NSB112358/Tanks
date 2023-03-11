import pygame

from Tanks import Tank


def driving(tank: Tank):
    keys = pygame.key.get_pressed()

    UP, DOWN, LEFT, RIGHT = keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d]

    speed = 5

    if sum([UP, DOWN, LEFT, RIGHT]) > 1:
        speed /= 2

    if UP:
        tank.rect.y -= speed
    if RIGHT:
        tank.rect.x += speed
    if DOWN:
        tank.rect.y += speed
    if LEFT:
        tank.rect.x -= speed