import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen , "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20,50)
            ast_1_vel = self.velocity.rotate(rand_angle)
            ast_2_vel = self.velocity.rotate(-rand_angle)
            ast_rad = self.radius - ASTEROID_MIN_RADIUS
            ast_1 = Asteroid(self.position.x, self.position.y, ast_rad)
            ast_2 = Asteroid(self.position.x, self.position.y, ast_rad)
            ast_1.velocity = ast_1_vel*1.2
            ast_2.velocity = ast_2_vel*1.2