import pygame
import sys
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    new_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    new_ast_feild = AsteroidField()

    fps_clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        
        for objects in drawable:
            objects.draw(screen)

        updatable.update(dt)

        for objects in asteroids:
            if objects.collides_with(new_player):
                log_event("player_hit")
                print("Game Over")
                sys.exit()
        
        for objects in asteroids:
            for bullet in shots:
                if objects.collides_with(bullet):
                    log_event("asteroid_shot")
                    bullet.kill()
                    objects.split()

        pygame.display.flip()

        dt = fps_clock.tick(60)/1000

if __name__ == "__main__":
    main()
