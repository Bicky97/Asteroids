import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.display) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first_new_vector = self.velocity.rotate(random.uniform(20, 50))
            second_new_vector = self.velocity.rotate(-random.uniform(20, 50))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
            first_asteroid.velocity = first_new_vector * 1.2
            second_asteroid.velocity = second_new_vector
