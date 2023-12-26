import pygame

# print("Hello world")

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The First Game")

WHITE = (255, 255, 255)

#This is to control how quickly the game updates the screen
FPS = 60

def draw_window():
    WIN.fill(WHITE)
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

