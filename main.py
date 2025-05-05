# this allows us to use code from
# the open-source pygame library
# throughout this file
# testing git
import sys
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
   
    Shot.containers = (shots,updatable,drawable)

    dt = 0
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")
    
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
