import Classes.Tanks as T
import random

# общий пулл танков
tanks = []

# Выбор нашего танка
my_tank = T.ST()

# инициализация танков
for i in range(10):
    random_seed = random.randint(0,2)
    tank = (T.LT, T.ST, T.TT)[random_seed]()
    tank.team = (T.TankTeam.GREEN, T.TankTeam.RED)[i % 2]
    tank.point.x = random.randint(1, 100)
    tank.point.y = random.randint(1, 48)
    tanks.append(tank)

# вставляем в общий пулл наш танк и подключаем управление
tanks.append(my_tank)

