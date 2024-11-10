from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.position), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt