import pygame


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

    # Параметры квадрата
    square_size = 30
    square_one_x = WIDTH // 10
    square_one_y = HEIGHT // 10

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
                elif event.key == pygame.K_s:  # Движение вниз (S)
                    square_one_y += STEP

        # Очистка экрана
        screen.fill("darkgreen")

        # Отрисовка квадрата
        pygame.draw.rect(screen, KUBIC, (square_one_x, square_one_y, square_size, square_size))

        # Обновление экрана
        pygame.display.flip()

        # Ограничение FPS
        clock.tick(30)

    pygame.quit()  # Теперь pygame.quit() внутри main()

if __name__ == "__main__":
    main()

