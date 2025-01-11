import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if radius == ASTEROID_MAX_RADIUS:
            self.colour = "blue"
        elif radius == ASTEROID_MIN_RADIUS * 2:
            self.colour = "purple"
        else:
            self.colour = "pink"

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            angle = random.uniform(20, 50)
            velocity_1 = self.velocity.rotate(angle)
            velocity_2 = self.velocity.rotate(-angle)
            asteroid_1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            asteroid_1.velocity = velocity_1 * 1.2
            asteroid_2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            asteroid_2.velocity = velocity_2 * 1.2


