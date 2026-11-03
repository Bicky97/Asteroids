import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    # to initialize the modules in the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0
    # delta to compute differences

    updatable = pygame.sprite.Group()
    # a container class that holds multiple updatable Sprite objects
    drawable = pygame.sprite.Group()
    # a container class that holds multiple drawable sprite objects

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    # a container class that holds multiple asteroid sprite objects
    Asteroid.containers = (asteroids, updatable, drawable)

    asteroidfield = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    AsteroidFields = AsteroidField()

    while True:
        # this is the game loop
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        # refreshes the screen
        dt = clock.tick(60) / 1000
        # method returns the amount of time has passed since the lst time it was called
        # the delta time



if __name__ == "__main__":
    main()
# this line ensures that the main function is called only when this file is run directly
# it won't run if it's imported as a module
