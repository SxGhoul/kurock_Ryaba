import pygame
import time


def show_loading_screen(screen):
    pygame.font.init()
    font = pygame.font.Font("doc1/Load_font.ttf", 35)

    screen.fill((0, 0, 0))
    text1 = font.render("Добро пожаловать в Labir.int!", True, (255, 255, 255))
    screen.blit(text1, (screen.get_width() // 2 - text1.get_width() // 2, screen.get_height() // 2))
    pygame.display.flip()
    time.sleep(2)

    screen.fill((0, 0, 0))
    text2 = font.render("Сделайте звук тише!", True, (255, 255, 255))
    screen.blit(text2, (screen.get_width() // 2 - text2.get_width() // 2, screen.get_height() // 2))
    pygame.display.flip()
    time.sleep(3)


def load_background_img(url):
    maze = pygame.image.load(url).convert()
    mask = pygame.mask.from_threshold(maze, (0, 0, 0, 255), (1, 1, 1, 255))
    return maze, mask


def check_collision_with_black(mask, x, y, size, margin=0):
    width, height = mask.get_size()

    for i in range(-margin, size + margin):
        for j in range(-margin, size + margin):
            new_x, new_y = x + i, y + j

            if 0 <= new_x < width and 0 <= new_y < height:
                if mask.get_at((new_x, new_y)):
                    return True
    return False


def main():
    pygame.init()
    pygame.mixer.init()
    collision_sound = pygame.mixer.Sound("doc1/Death_sound.mp3")
    level_up_sound = pygame.mixer.Sound("doc1/Teleport_sound.mp3")

    WIDTH, HEIGHT = 700, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Labir.int")

    show_loading_screen(screen)

    clock = pygame.time.Clock()
    running = True

    STEP = 3

    maze_path = ["doc1/de_lab_01.png", "doc1/de_lab_02.png"]
    spawn_points = [(18, 3), (650, 430)]

    current_maze_index = 0
    maze, mask = load_background_img(maze_path[current_maze_index])

    square_size = 30
    square_one_x, square_one_y = spawn_points[current_maze_index]

    player_img = pygame.image.load("doc1/Player.jpg")
    player_img = pygame.transform.scale(player_img, (square_size, square_size))

    green_square_size = 30
    green_square_x = 690
    green_square_y = 432

    margin = -5

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    keys = {pygame.K_w: False, pygame.K_s: False, pygame.K_a: False, pygame.K_d: False}

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keys[event.key] = True
            elif event.type == pygame.KEYUP:
                keys[event.key] = False

        prev_x, prev_y = square_one_x, square_one_y

        if keys[pygame.K_a]:
            square_one_x -= STEP
        if keys[pygame.K_d]:
            square_one_x += STEP
        if keys[pygame.K_w]:
            square_one_y -= STEP
        if keys[pygame.K_s]:
            square_one_y += STEP

        if check_collision_with_black(mask, square_one_x, square_one_y, square_size, margin):
            pygame.mixer.Sound.play(collision_sound)
            square_one_x, square_one_y = spawn_points[current_maze_index]

        player_rect = pygame.Rect(square_one_x, square_one_y, square_size, square_size)
        green_square_rect = pygame.Rect(green_square_x, green_square_y, green_square_size, green_square_size)

        if player_rect.colliderect(green_square_rect) and current_maze_index < len(maze_path) - 1:
            current_maze_index += 1
            pygame.mixer.Sound.play(level_up_sound)
            maze, mask = load_background_img(maze_path[current_maze_index])
            square_one_x, square_one_y = spawn_points[current_maze_index]

        screen.fill(WHITE)
        screen.blit(maze, (0, 0))
        pygame.draw.rect(screen, GREEN, (green_square_x, green_square_y, green_square_size, green_square_size))
        screen.blit(player_img, (square_one_x, square_one_y))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()