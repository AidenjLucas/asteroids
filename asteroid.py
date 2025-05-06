import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius,spawn_protection):
        super().__init__(x, y, radius)
        self.spawn_protection = spawn_protection
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        
        self.position += self.velocity * dt

        if self.spawn_protection < 0:
            if self.position.x > SCREEN_WIDTH:
                self.position.x = 0
            elif self.position.x < 0:
                self.position.x = SCREEN_WIDTH

            if self.position.y > SCREEN_HEIGHT:
                self.position.y = 0
            elif self.position.y < 0:
                self.position.y = SCREEN_HEIGHT
           
        if self.spawn_protection > 0: self.spawn_protection -= 0.1

    def split(self,score):
        score.points += 5
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20,50)

        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x,self.position.y,new_radius,0)
        asteroid2 = Asteroid(self.position.x,self.position.y,new_radius,0)

        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2