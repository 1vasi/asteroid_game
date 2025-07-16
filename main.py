import pygame
from constants import *
pygame.init()
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0 

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable)
    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip() 
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
   main()
