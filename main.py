# this allows us to use code from
# the open-source pygame library
# throughout this file
# testing git
import pygame
from constants import *
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    play = player.Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        screen.fill("black")
        play.update(dt)
        play.draw(screen)

        pygame.display.flip()

        
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
