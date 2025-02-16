import pygame

def load_background_img(url):
    maze = pygame.image.load(url).convert()
    mask = pygame.mask.from_threshold(maze, (0, 0, 0, 255), (1, 1, 1, 255))
    return maze, mask


def main():
    pygame.init()

    # Размеры окна
    WIDTH, HEIGHT = 700, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Labir.int")

    clock = pygame.time.Clock()
    running = True

    # Скорость движения
    STEP = 10

    maze, mask = load_background_img("Fon555566.png")

    # Параметры квадрата
    square_size = 30
    square_one_x = WIDTH // 10
    square_one_y = HEIGHT // 10

    square_one_x = 10
    square_one_y = 10
    start_x, start_y =square_one_x, square_one_y

    player_img = pygame.image.load("lolo.png")
    player_img = pygame.transform.scale(player_img, (square_size, square_size))



    # Цвета
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    KUBIC = (87, 88, 110)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  # Движение влево (A)
                    square_one_x -= STEP
                elif event.key == pygame.K_d:  # Движение вправо (D)
                    square_one_x += STEP
                elif event.key == pygame.K_w:  # Движение вверх (W)
                    square_one_y -= STEP
                elif event.key == pygame.K_s:
                    square_one_y += STEP

        pygame.display.flip()


        screen.blit(maze, (0, 0))
        screen.blit(player_img, (square_x, square_y))

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()

