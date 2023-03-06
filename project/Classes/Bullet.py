from enum import Enum
from Classes.General import point

class BulletVector(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Bullet():
    def __init__(self, x: int, y: int, vector: BulletVector, speed: int = 1) -> None:
        self.point = point(x, y)
        self.vector = vector
        self.speed = speed