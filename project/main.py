import Classes.Tanks as T
import Classes.Map as M
import keyboard

from config import tanks, my_tank
from os import system

clear = lambda: system('cls')

def on_key(event):

    key = str(event.name).lower()

    if key not in ('w','s','d','a'):
        return

    # Изменяет состояние координат нашего танка
    match str(event.name):
        case 'w':
            if my_tank.point.y > 1:
                my_tank.point.y -= 1
        
        case 's':
            if my_tank.point.y < 50:
                my_tank.point.y += 1
        
        case 'a':
            if my_tank.point.x > 1:
                my_tank.point.x -= 1
        
        case 'd':
            if my_tank.point.x < 100:
                my_tank.point.x += 1

    clear()
    map.view(tanks)


# Создаем карту
map = M.Map()

# Настраиваем наш танк
my_tank.point.x = 10
my_tank.point.y = 10
my_tank.team = T.TankTeam.I

# Первичное отображение
map.view(tanks)

# Подключаем управление 
keyboard.on_press(on_key)

# Запуск игры
keyboard.wait()