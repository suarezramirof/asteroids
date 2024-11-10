import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable)

    Shot.containers = (updatable, drawable, shots)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)

    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for sprite in drawable.sprites():
            sprite.draw(screen)
        for sprite in updatable.sprites():
            sprite.update(dt)
        for asteroid in asteroids.sprites():
            if asteroid.check_collision(player):
                print("Game over")
                return
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
                    
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()