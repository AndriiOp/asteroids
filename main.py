import pygame
print("Starting asteroids!")
from player import Player

from constants import * #import all constants from constants.py file
def main():
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
       screen.fill((0, 0, 0))
       updatable.update(dt)
       for entity in drawable:
            entity.draw(screen)
       pygame.display.flip()
       dt = clock.tick(60) / 1000 
       


if __name__ == "__main__":
    main()