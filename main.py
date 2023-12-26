import pygame
#This imports operating system which allows you to define the path to the images folder
import os

# print("Hello world")

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The First Game")

WHITE = (255, 255, 255)

#This is to control how quickly the game updates the screen
FPS = 60

#Import images of ships
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assests', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assests', 'spaceship_red.png'))

def draw_window(): 
    
    WIN.fill(WHITE)
    WIN.blit()
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

