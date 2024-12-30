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
        out = [self.character_positions]
        if x > 0:
            out.append("n")
        if x [0] > 0:
            out.append("s")
        if y [1] < 0:
            out.append("e")
        if y [1] > 0:
            out.append("w")
        return out




class Cam:
    
    def __init__(self, game_map, ):
        self.game_map = game_map["game_map"]
        self.player = Player()
        self.view_port = [[[]]]

    def create_view_port(self,view_size = [0,0],view_position=[0,0]):
        self.view_size = view_size
        self.view_position = view_position
        for self.view_position[0] in range(self.view_size[0]):
            for self.view_position[1] in range(self.view_size[1]):
                for iz in range(self.game_map[0][0]):
                    self.view_port.append(self.game_map[0][0][0])
                
        return self.view_port



    
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
    pprint(c.create_view_port())