import pygame,sys
from pygame import *

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = display.set_mode((400,400))
    pygame.display.set_caption("REVIEW")
    player = pygame.image.load('blocks.png')
    location = [100,100]
    moving_right = False # this part

    while True:

        screen.fill((146,244,255))
        screen.blit(player, location)
        pygame.display.update()

        if moving_right == True: #this if statement and expression 
            location[0] += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()   

            if event.type == KEYDOWN: #keydown
                if event.key == K_RIGHT:
                    moving_right = True # it's true when K_RIGHT is held down
            if event.type == KEYUP: # keyup 
                if event.key == K_RIGHT: # false when K_RIGHT is let go
                    moving_right = False


        clock.tick(60)


main()