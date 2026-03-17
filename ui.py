import os
import time
import pygame
import sys

BRUTAL = r"""  
                        ____                   __        __                  _     
                       / __ )____  ____  _____/ /_  ____/ /___ _____ _      (_)___ 
                      / __  / __ \/ __ \/ ___/ __ \/ __  / __ `/ __ `/_____/ / __ \
                     / /_/ / /_/ / /_/ (__  ) / / / /_/ / /_/ / /_/ /_____/ / /_/ /
                    /_____/\____/\____/____/_/ /_/\__,_/\__,_/\__, /     /_/\____/ 
                                          /____/
__  __                    _____ __             __
                   \ \/ /___  __  _______   / __(_) /__  _____   / /_  ____ __   _____ 
                    \  / __ \/ / / / ___/  / /_/ / / _ \/ ___/  / __ \/ __ `/ | / / _ \
                    / / /_/ / /_/ / /     / __/ / /  __(__  )  / / / / /_/ /| |/ /  __/
                   /_/\____/\__,_/_/     /_/ /_/_/\___/____/  /_/ /_/\__,_/ |___/\___/ 

                      __                                                        __           ____
                     / /_  ___  ___  ____     ___  ____  ____________  ______  / /____  ____/ / /
                   / __ \/ _ \/ _ \/ __ \   / _ \/ __ \/ ___/ ___/ / / / __ \/ __/ _ \/ __  / /
                 / /_/ /  __/  __/ / / /  /  __/ / / / /__/ /  / /_/ / /_/ / /_/  __/ /_/ /_/
               /_.___/\___/\___/_/ /_/   \___/_/ /_/\___/_/   \__, / .___/\__/\___/\__,_(_)
                                         /____/_/

"""
VERDE  = (0, 255, 70)
NEGRO  = (0, 0, 0)

def terminal():
    pygame.init()

    info = pygame.display.Info()
    pantalla = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN | pygame.NOFRAME)
    pygame.display.set_caption("ROOT SECURITY")

    FONT_SIZE = 14
    try:
        fuente = pygame.font.SysFont("Courier New", FONT_SIZE, bold=True)
    except:
        fuente = pygame.font.SysFont("monospace", FONT_SIZE, bold=True)

    lineas = BRUTAL.splitlines()
    lineas_renderizadas = []

    pantalla.fill(NEGRO)
    pygame.display.flip()

    ancho_pantalla = info.current_w
    alto_pantalla  = info.current_h
    alto_total     = len(lineas) * (FONT_SIZE + 2)
    y_inicio       = max(0, (alto_pantalla - alto_total) // 2)
    clock = pygame.time.Clock()

    for i, linea in enumerate(lineas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()

        superficie = fuente.render(linea, True, VERDE)
        x = (ancho_pantalla - superficie.get_width()) // 2
        y = y_inicio + i * (FONT_SIZE + 2)
        pantalla.blit(superficie, (x, y))
        pygame.display.flip()
        clock.tick(60)
        time.sleep(0.1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()
        clock.tick(30)

if __name__ == "__main__":
    terminal()