from enum import Enum
from Classes.Bullet import Bullet as B, BulletVector as BV
from Classes.General import point

class TankList(Enum):
    LT = 0
    ST = 1
    TT = 2


class TankTeam(Enum):
    NONE = -1
    RED = 0
    GREEN = 1
    I = 2


class Tank():
    
    def __init__(self) -> None:
        self.HP = 100
        self.speed = 2
        self.point = point(0, 0)
        self.team = TankTeam.NONE
        self.bullet_list = []


    def shoot(self, vector: BV) -> None:
        new_bullet = B(self.x, self.y, vector)

        match vector:
            case BV.UP:
                new_bullet.point.y -= 1
            case BV.DOWN:
                new_bullet.point.y += 1
            case BV.LEFT:
                new_bullet.point.x -= 1
            case BV.RIGHT:
                new_bullet.point.x += 1        

        self.bullet_list.append(new_bullet)


    def bullet_move(self, tanks) -> None:

        for bullet in self.bullet_list:
            match bullet.vector:
                case BV.UP:
                    bullet.point.y -= 1
                case BV.DOWN:
                    bullet.point.y += 1
                case BV.LEFT:
                    bullet.point.x -= 1
                case BV.RIGHT:
                    bullet.point.x += 1  

            for tank in tanks:
                pass



class LT(Tank):

    def __init__(self) -> None:
        super().__init__()
        self.speed = 3
        self.damage = 15
        self.tank_class = TankList.LT

class ST(Tank):

    def __init__(self) -> None:
        super().__init__()
        self.damage = 20
        self.tank_class = TankList.ST

class TT(Tank):

    def __init__(self) -> None:
        super().__init__()
        self.speed = 1
        self.damage = 25
        self.tank_class = TankList.TT