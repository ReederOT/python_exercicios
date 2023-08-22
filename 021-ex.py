print('='*30)
print('Exercicio - 21')
print('\nCrie um programa em Python que abra, e reproduza o audio de arquivo mp3.')
print('='*30)

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait


