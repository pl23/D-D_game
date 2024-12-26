import pygame

def events(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            running = True
    return [running,]

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        while self.running:
            if events(self.running) 

            self.screen.fill("purple")
            pygame.display.flip()
            self.clock.tick(60) 

        pygame.quit()

Game()