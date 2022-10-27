import pygame
import sys

from config import *
from gameEngine import Game

# Main class where will be accure all types of objects
class Main:
    # Constructor, here described capture a screen method
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
        pygame.display.set_caption('Chess game')
        self.game = Game()
        
    # Launch programm
    def mainloop(self):
        while True:
            # Render a pieces
            self.game.field(self.screen)
            self.game.pieces(self.screen)
            self.game.dragger(self.screen)
            
            # For exiting from programm
            for event in pygame.event.get():
                # Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                # Mouse motion
                if event.type == pygame.MOUSEMOTION:
                    pass
                # Click release
                if event.type == pygame.MOUSEBUTTONUP:
                    pass
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
    
if __name__ == "__main__":
    main = Main()
    main.mainloop()