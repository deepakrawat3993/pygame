import pygame
import os
from math import pi
pygame.init()

window = pygame.display.set_mode((600,600))
pygame.display.set_caption("My first game ever")
x = 50
y = 50
width = 40
height = 50
vel = 20
run = True

img = pygame.image.load("ufo.png")
img = pygame.transform.scale(img,(50,50))

bg = pygame.image.load("space.jpg")

asteriod = pygame.image.load("asteriod.png")
asteriod = pygame.transform.scale(asteriod,(50,50))
pygame.mixer.music.load("spaceship_sound.mp3")
pygame.mixer.music.play(0)
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=vel
        pygame.mixer.music.load("launch_sound.mp3")
        pygame.mixer.music.play(0)
        pygame.mixer.music.stop()

    if keys[pygame.K_RIGHT]:
        x+=vel

    if keys[pygame.K_UP]:
        y-=vel

    if keys[pygame.K_DOWN]:
        y+=vel
    window.fill((100,150,200))
    window.blit(bg,(0,0))
    window.blit(img,(x,y))

    pygame.draw.line(window, (34, 33, 32), [50, 500], [500, 500], 10)
    pygame.draw.line(window, (34,33,32), [0, 400], [400,400], 10)

    window.blit(asteriod, (300, 450))
    window.blit(asteriod, (200, 200))
    window.blit(asteriod, (300, 240))

    pygame.draw.line(window, (34, 33, 32), [0, 100], [300, 100], 10)
    pygame.draw.line(window, (34, 33, 32), [500, 300], [100, 300], 10)
    pygame.display.update()
pygame.quit()