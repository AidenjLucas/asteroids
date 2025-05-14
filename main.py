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
from score import *


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
    Score.containers = (updatable,drawable)
    score = Score()
    prev_score = score.points   

    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("img/Blue_Nebula4.png") 
    background = background.convert_alpha()
    
    
    dt = 0

    pygame.display.set_caption(f"Asteroids | Score: {score.points} | lives : {player.lives}")
    
    while(True):
        
        if score.points != prev_score: pygame.display.set_caption(f"Asteroids | Score: {score.points} | lives : {player.lives}")

        prev_score = score.points

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                respawn(asteroids,player)
                pygame.display.set_caption(f"Asteroids | Score: {score.points} | lives : {player.lives}")
            if player.lives < 1:
                print(f"Game Over! Your score was {score.points}")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split(score)
                    shot.kill()
        
        
        screen.fill("black")
        screen.blit(background,(0,0))
        screen.blit(background,(1024,0))
        
        
        for object in drawable:
             object.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


def respawn(asteroids,player):
    
    for asteroid in asteroids:
        asteroid.kill()

    player.lives -= 1
    player.position = pygame.Vector2(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    player.rotation = 0

    asteroids.empty()
    

if __name__ == "__main__":
    main()




    