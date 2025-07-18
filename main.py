import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import * 
from circleshape import *

pygame.init()
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0 

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfeild = AsteroidField()
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        

        for self in drawable:
            self.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.colision_check(player1) == True: 
                print("Game over!")
                pygame.quit()
                
        
        pygame.display.flip() 
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
   main()
