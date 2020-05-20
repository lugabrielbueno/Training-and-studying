#Playing music

import pygame

pygame.mixer.init()
pygame.mixer.music.load('alarm.mp3')
pygame.mixer.music.play()
input()