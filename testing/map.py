class player:
    def __init__(self,cam):
        self.map = map
        self.character_positions = [None,None]
    def move(self,x,y):
        self.character_positions += [x,y]


class cam:
     def __init__(self,map):
         


        

map = {
    [
        [["grass",True,"player"],["grass",True,],["grass",True,],[None],[None],[None],[None],[None],[None],[None],],
        [["grass",True,],["grass",True,],["grass",True,],[None],[None],[None],[None],[None],[None],[None],],
        [["grass",True,],["grass",True,],["grass",True,],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
    ]
}
player(map)