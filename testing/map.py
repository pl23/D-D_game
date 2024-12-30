from pprint import pprint
from copy import deepcopy 
import json, numpy

path = "map.json"
class Player:
    def __init__(self,):
        self.character_positions = [None,None]
        self.player_direction = None
    def move(self,x,y):
        self.character_positions += [x,y]
        if x > 0:
            self.player_direction = "right"
        elif x < 0:
            self.player_direction = "left"
        elif y > 0:
            self.player_direction = "down"
        elif y < 0:
            self.player_direction = "up"
        

class Cam:
    def __init__(self, game_map, ):
        self.game_map = game_map["game_map"]
        self.player = Player()
        self.view_port = [[[]]]
        self.view_size = [5,5]
        self.view_position = [0,0]
        
    def update_view_port(self):
        for x in range(self.view_size[0]):
            for y in range(self.view_size[1]):
                for z in range(len(self.game_map[x][y])):
                    self.view_port[x][y].append(self.game_map[x][y][z])
        pprint(self.view_port)
    
    def move_view_port(self, ):
        pass
        
        
    

    def move_player (self):
        pass

    def p(self):
        pprint(self.view_port)







data = {"game_map":[
        [["grass",True,"player"],["grass",True,],["grass",True,],[None],[None],[None],[None],[None],[None],[None],],
        [["grass",True,],["grass",True,],["grass",True,],[None],[None],[None],[None],[None],[None],[None],],
        [["grass",True,],["grass",True,],["grass",True,],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],
        [[None],[None],[None],[None],[None],[None],[None],[None],[None],[None],],]
}
class J:
    def __init__(self):
        pass
    def l(self):
        with open(path, "r") as f:
            data = json.load(f)
        return data

if __name__ == "__main__":
    c = Cam(data)
    c.update_view_port()
    c.p()