import pygame
import datetime
import math


pygame.init()
screen = pygame.display.set_mode((800, 800))

background_image = pygame.image.load('C:\\VScode_programs\\Python\\lib\\tsis7\\clock.png').convert()
screen.blit(background_image, (392, 388))


min = pygame.image.load('C:\\VScode_programs\\Python\\lib\\tsis7\\minute.png')
minrec = min.get_rect()
minrec.center=(392,388)


sec = pygame.image.load('C:\\VScode_programs\\Python\\lib\\tsis7\\second.png')
secrec = sec.get_rect()
secrec.center=(392,388)



currt=datetime.datetime.now()
seccnt=currt.second
mincnt=currt.minute


clock = pygame.time.Clock()
done = False



def convert_degrees(R, alpha):
    x=math.sin(math.pi*alpha/180)*R
    y=math.cos(math.pi*alpha/180)*R
    return x+400-10, 400-y-15

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image, (-250, -95))

    sec1=pygame.transform.rotate(sec, -1*(6*seccnt+180))
    secrec1=sec1.get_rect()
    secrec1.center=secrec.center
    screen.blit(sec1, secrec1)
    min1=pygame.transform.rotate(min, -1*(6*mincnt))
    minrec1=min1.get_rect()
    minrec1.center=minrec.center
    screen.blit(min1, minrec1)
    currt=datetime.datetime.now()
    seccnt=currt.second
    seccnt-=30
    mincnt=currt.minute
    mincnt-=15

    pygame.display.update()
    clock.tick(60)