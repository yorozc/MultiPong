import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
    
    def run(self):
        clock = pygame.time.Clock()
        while(self.running):
            for event in pygame.event.get():
                pass


        
        pygame.display.flip()
        clock.tick(0)
        
if __name__ == "__main__":
    game = Game()
    game.run()