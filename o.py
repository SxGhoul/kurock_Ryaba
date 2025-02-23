import pygame


def load_background_img(url):
    maze = pygame.image.load(url).convert()
    mask = pygame.mask.from_threshold(maze, (0, 0, 0, 255), (1, 1, 1, 255))
    return maze, mask


def check_collision_with_black(mask, x, y, size, margin=0):
    """Проверяет, есть ли чёрный цвет в области спрайта с зазором (margin)"""
    for i in range(-margin, size + margin):
        for j in range(-margin, size + margin):
            if mask.get_at((x + i, y + j)):
                return True
    return False


def main():
    pygame.init()

    # Размеры окна
    WIDTH, HEIGHT = 700, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Labir.int")

    clock = pygame.time.Clock()
    running = True

    # Скорость движения
    STEP = 3

    # Пути к уровням и точки спавна
    maze_path = ["doc1/de_lab_01.png", "doc1/de_lab_02.png"]
    spawn_points = [(18, 3), (650, 440ыв)]  # Координаты спавна для каждого уровня

    current_maze_index = 0
    maze, mask = load_background_img(maze_path[current_maze_index])

    # Параметры игрока
    square_size = 30
    square_one_x, square_one_y = spawn_points[current_maze_index]

    # Изображение игрока
    player_img = pygame.image.load("doc1/131.jpg")
    player_img = pygame.transform.scale(player_img, (square_size, square_size))

    green_square_size = 30
    green_square_x = 690
    green_square_y = 432

    # Настройка чувствительности к черному цвету
    margin = -5  # Увеличивает зону проверки на 3 пикселя (можно уменьшить до 0 или -3)

    # Цвета
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    # Список нажатых клавиш
    keys = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keys[event.key] = True
            elif event.type == pygame.KEYUP:
                keys[event.key] = False

        # Движение игрока
        prev_x, prev_y = square_one_x, square_one_y  # Запоминаем старые координаты

        if keys[pygame.K_a]:  # Влево
            square_one_x -= STEP
        if keys[pygame.K_d]:  # Вправо
            square_one_x += STEP
        if keys[pygame.K_w]:  # Вверх
            square_one_y -= STEP
        if keys[pygame.K_s]:  # Вниз
            square_one_y += STEP

        # Проверка перехода на следующий уровень
        player_rect = pygame.Rect(square_one_x, square_one_y, square_size, square_size)
        green_square_rect = pygame.Rect(green_square_x, green_square_y, green_square_size, green_square_size)

        if player_rect.colliderect(green_square_rect) and current_maze_index < len(maze_path) - 1:
            current_maze_index += 1
            maze, mask = load_background_img(maze_path[current_maze_index])
            square_one_x, square_one_y = spawn_points[current_maze_index]  # Новый спавн

        screen.fill(WHITE)
        screen.blit(maze, (0, 0))
        pygame.draw.rect(screen, GREEN, (green_square_x, green_square_y, green_square_size, green_square_size))
        screen.blit(player_img, (square_one_x, square_one_y))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()




