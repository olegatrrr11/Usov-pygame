import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
razmer = 10
speed = 15
x = 300
y = 200
x_kub = 0
y_kub = 0

x_random = round(random.randrange(0, 600 - razmer) / 10) * 10
y_random = round(random.randrange(0, 400 - razmer) / 10) * 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_kub = -razmer
                y_kub = 0
            elif event.key == pygame.K_RIGHT:
                x_kub = razmer
                y_kub = 0
            elif event.key == pygame.K_UP:
                y_kub = -razmer
                x_kub = 0
            elif event.key == pygame.K_DOWN:
                y_kub = razmer
                x_kub = 0

    x += x_kub
    y += y_kub
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), [x_random, y_random, razmer, razmer])
    pygame.draw.rect(screen, (0, 0, 0), [x, y, razmer, razmer])
    pygame.display.update()
    clock.tick(speed)
