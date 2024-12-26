import json
class Map:
    def __init__(self,path):
        self.path = path
        self.map_aray = {}
    
    
    def load_map(self):
        with open(f"{self.path}") as f:
            data = json.loads(f)
            self.map = data
    
class test:
    def __init__(self,path):
        self.path = path
        self.map_aray = {[
            [[]]
    ]}
    
    
    def load_map(self):
        with open(f"{self.path}") as f:
            data = json.loads(f)
            self.map = data
    

