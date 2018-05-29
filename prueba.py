#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *

# Constantes
WIDTH = 900
HEIGHT = 500


def imagen(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except Exception as e:
        raise SystemExit(e)

    image = image.convert()

    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, pygame.RLEACCEL)

    return image

# Clases
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Tutorial parte 2")

    fondo = imagen("imagenes/fondo.png").convert()
    mario = imagen("imagenes/mario.png")

    fondo = pygame.transform.scale(fondo, (1000, 400))

    screen.blit(fondo, (0,0))
    screen.blit(mario, (100,304))

    pygame.display.flip()

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

    return 0

def pantalla():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Prueba Pygame")

    return 0

if __name__ == '__main__':
    main()
