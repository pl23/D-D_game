class player:
    def __init__(self,vew):
        self.map = map
        self.character_positions = [None,None]
    def move(self,x,y):
        self.character_positions += [x,x]


class cam:
     def __init__(self,map):
        self.vew = [[[]]]
        self.vew_position = []
        self.vew_size = [5,5]
		for x in range(vew_size[0]:):
            for y in range(vew_size[1]):
                for z in len map[x][y][z]:
                    vew.apend(map[x][y][z])
    

         


        

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
