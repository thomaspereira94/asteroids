import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from shot import Shot


def main():
    pygame.init()
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()
    #infinite loop to keep game window open
    loop_counter = 0
    while loop_counter == 0:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()   
        updatable.update(delta_time)

        for item in asteroids:
            if player.colides_with(item):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            log_event("asteroid_shot")
            
            for shot in shots:
                if asteroid.colides_with(shot):
                    shot.kill()
                    asteroid.split()

        delta_time = game_clock.tick(60) / 1000

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
