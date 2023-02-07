import pygame, sys
from PIL import Image

from pygame.constants import K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT

WINDOW_SIZE = (600,800)

pygame.init()
display = pygame.display.set_mode(WINDOW_SIZE)

def main():

    display.fill((146,244,255))
    clock = pygame.time.Clock()
    starting_location = (280, 700)
    object1 = pygame.Rect((20, 50), (50, 100))  

    while True:
        display.blit(object1, starting_location)

        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        

        pygame.display.update()
        clock.tick(60)



main()