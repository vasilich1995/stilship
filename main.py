import pygame

import random
import os

WIDTH = 1080
HEIGHT = 720


game_folder  = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,'img')

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background_img = pygame.image.load(os.path.join(img_folder, 'background.png'))
background_img2 = pygame.image.load(os.path.join(img_folder, 'background.png'))
background_rect = background_img.get_rect()
background_rect2 = background_img.get_rect()

clock = pygame.time.Clock()


background_rect2.x = WIDTH

background_rect.x = 0




while True:
    background_rect.x-=3
    background_rect2.x-=3
    if background_rect.x == -WIDTH:
        background_rect.x = WIDTH
    if background_rect2.x == -WIDTH:
        background_rect2.x = WIDTH


    screen.blit(background_img, background_rect)
    screen.blit(background_img2, background_rect2)
    pygame.display.update()
    clock.tick(25)
    print(background_rect.x)
    print(background_rect2.x)