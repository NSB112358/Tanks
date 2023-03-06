import pygame

pygame.init()

# Размер окна
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Моя игра")

# Цикл, пока пользователь не нажмет кнопку закрытия окна
done = False

# Используется для управления частотой обновления экрана
clock = pygame.time.Clock()

# Основной цикл программы
while not done:
    # --- Главный цикл обработки событий ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Логика игры здесь ---

    # --- Рисование здесь ---

    # --- Конец рисования ---

    # Ограничение до 60 кадров в секунду
    clock.tick(60)

# Закрываем окно и выходим.
pygame.quit()
