""" Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3."""

import pygame

musica = 'musica.mp3'
def tocaMusica(musica):
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    print('A música está sendo tocada..')
    pygame.event.wait()
    print('Fim da música')

tocaMusica(musica)








