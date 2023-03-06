import Classes.Tanks as T

class Map():
    def __init__(self) -> None:
        self.map = ""

        for i in range(52):        # | —
                
            if i == 0 or i == 51:
                self.map += '—' * 102 + '\n'

            else:
                self.map += '|' + ' ' * 100 + '|\n'

    
    def print(self):
        print(self.map)


    def view(self, tanks: list[T.Tank]):
        map_list = self.map.split('\n')

        for tank in tanks:
            x = tank.point.x
            y = tank.point.y

            tank_s = ''
            match tank.tank_class:
                 
                case T.TankList.LT:
                    tank_s = "L"

                case T.TankList.ST:
                	tank_s = "S"

                case T.TankList.TT:
                	tank_s = "T"
                        
            # https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
            if tank.team == T.TankTeam.RED:
                tank_s = f"\033[31m{tank_s}\033[0m"
            elif tank.team == T.TankTeam.GREEN:
                tank_s = f"\033[32m{tank_s}\033[0m"
            elif tank.team == T.TankTeam.I:
                tank_s = f"\033[34m{tank_s}\033[0m"

            map_list[y] = map_list[y][:x] + tank_s + map_list[y][x+1:]

        print('\n'.join(map_list))