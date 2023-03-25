from enum import Enum

class TankClass(Enum):
    LT = 1
    ST = 2
    TT = 3

class Bullet():
    def __init__(self, X, Y) -> None:
        self.X = X
        self.Y = Y

class Tank():
    def __init__(self, tank_class: TankClass) -> None:
        match tank_class:
            case TankClass.LT:
                self.hp = 80
                self.damage = 20
                self.speed = 4

            case TankClass.ST:
                self.hp = 100
                self.damage = 30
                self.speed = 2
            
            case TankClass.TT:
                self.hp = 120
                self.damage = 40
                self.speed = 1

        self.bullets = []