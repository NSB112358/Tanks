import pygame

from Tanks import Tank
from Controls import driving

pygame.init()

# Размер окна
size = (700, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Моя игра")

# Цикл, пока пользователь не нажмет кнопку закрытия окна
done = False

# Используется для управления частотой обновления экрана
clock = pygame.time.Clock()

player_tank = Tank(100, 100)
enemy_tank = Tank(500, 500)

# Основной цикл программы
while not done:
    # --- Главный цикл обработки событий ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Логика игры здесь ---
    driving(player_tank)
    

    # --- Рисование здесь ---
    screen.fill((0, 0, 0))

    screen.blit(player_tank.image, player_tank.rect)
    screen.blit(enemy_tank.image, enemy_tank.rect)

    pygame.display.flip()
    # --- Конец рисования ---

    # Ограничение до 60 кадров в секунду
    clock.tick(60)

# Закрываем окно и выходим.
pygame.quit()
