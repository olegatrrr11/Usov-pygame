import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

razmer = 10

#создаём пищу в образе яблока из корневой папки картникой image.png и уменьшаем его до состояния кубика
apple = pygame.image.load('image.png')
apple = pygame.transform.scale(apple, (razmer, razmer))

def draw_button(text, x, y, width, height):
    rect = pygame.Rect(x, y, width, height)
    if not rect.collidepoint(pygame.mouse.get_pos()):
        color = (255, 255, 255)
    else:
        color = (0, 200, 255)
    pygame.draw.rect(screen, color, rect)

    font = pygame.font.SysFont('Arial', 30)
    text_surface = font.render(text, True, (0, 255, 0))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

    return rect

#функция самого меню, где располагаются кнопки 'начать игру' и 'выход', после нажатия начать игру, начианется игра
#после нажатия выход, игра закрывается
def menu():
    while True:
        screen.fill((255, 255, 255))
        draw_text('Змейка', 50, (0, 0, 0), screen, 200, 50)

        b_start = draw_button('Начать игру', 200, 150, 200, 50)
        b_exit = draw_button('Выход', 200, 250, 200, 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_start.collidepoint(pygame.mouse.get_pos()):
                    game()
                if b_exit.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

def draw_text(text, size, color, surface, x, y):
    f = pygame.font.SysFont('Arial', size)
    text = f.render(text, True, color)
    surface.blit(text, (x, y))

def game():
    x = 300
    y = 200
    x_kub = 0
    y_kub = 0

    zmey = []
    dlina = 1

    x_random = round(random.randrange(0, 600 - razmer) / 10) * 10
    y_random = round(random.randrange(0, 400 - razmer) / 10) * 10

    schet = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_kub == 0:
                    x_kub = -razmer
                    y_kub = 0
                elif event.key == pygame.K_RIGHT and x_kub == 0:
                    x_kub = razmer
                    y_kub = 0
                elif event.key == pygame.K_UP and y_kub == 0:
                    y_kub = -razmer
                    x_kub = 0
                elif event.key == pygame.K_DOWN and y_kub == 0:
                    y_kub = razmer
                    x_kub = 0

        x += x_kub
        y += y_kub

        if x >= 600 or x < 0 or y >= 400 or y < 0:
            konec_igri(schet)

        for k in zmey[:-1]:
            if k == (x, y):
                konec_igri(schet)

        zmey.append((x, y))
        if len(zmey) > dlina:
            del zmey[0]

        if x == x_random and y == y_random:
            schet += 1
            dlina += 1
            x_random = round(random.randrange(0, 600 - razmer) / 10) * 10
            y_random = round(random.randrange(0, 400 - razmer) / 10) * 10

        screen.fill((255, 255, 255))
        for i in zmey:
            pygame.draw.rect(screen, (0, 255, 0), [i[0], i[1], razmer, razmer])

        screen.blit(apple, (x_random, y_random))

        draw_text(f'Счет: {schet}', 20, (0, 0, 0), screen, 10, 10)

        pygame.display.update()
        clock.tick(15)

def konec_igri(schet):
    menu()

menu()
