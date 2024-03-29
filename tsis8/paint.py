import pygame
import os
pygame.init()

screen = pygame.display.set_mode((900, 800))

clock = pygame.time.Clock()

RED = (230, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 230)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE]
color = WHITE

eraser = pygame.image.load('C:\\VScode_programs\\Python\\lib\\tsis8\\lastik.png')
eraser = pygame.transform.scale(eraser, (70, 70))

def draw_rect(index):
    pygame.draw.rect(screen, colors[index], (0, index*40, 40, 40))

def pick_color():
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if 0<=x<=40 and 0<=y<=40:
            return RED
        elif 40<x<=80 and 0<=y<=40:
            return GREEN
        elif 80<x<=120 and 0<=y<=40:
            return BLUE
        elif 1010<=x<=1080 and 0<=y<=40:
            return BLACK
        elif 130<=x<=170 and 0 <= y <= 40:
            return "rect"
    return color

def painting(color):
    click = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    if click[0]:
        if color != 'rect':
            pygame.draw.circle(screen, color, (x, y), 27)
        else:
            pygame.draw.rect(screen, WHITE, (y, x, 40, 40), 4)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    for i in range(len(colors)):
        draw_rect(i)
    screen.blit(eraser, (0, 200))
    pygame.draw.rect(screen, WHITE, (0, 130, 40, 40), 4)

    color = pick_color()
    painting(color)


    clock.tick(300)
    pygame.display.update()