
import pprint
class player:
    def __init__(self):
        import map
        self.map_class = map.test()
        self.map = self.map_class.map_aray
        self.x = xy[0]
        self.y = xy[1]
    def p(self):
        pprint(self.map)

def test():
    p=player()
    p.p()
test()