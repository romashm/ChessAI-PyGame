import pygame

from config import *
from piece import *
from square import Square
from dragger import Dragger

class Board:
    
    # Described values on the board ( for instance -> 0 no one in this piece, 1 vice versa)
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLUMNS)]
        
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")
    
    # Render event above, it's need to each piece receive value 0
    def _create(self):
        for row in range(ROWS):
            for col in range(COLUMNS):
                self.squares[row][col] = Square(row, col)
                
    # We render our pieces & put in inside game
    def _add_pieces(self, color):
        # Rows started by 0
        row_pawn, row_other = (6,7) if color == 'white' else (1,0)
        
        # pawns
        for col in range(COLUMNS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
            
        # Knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        
        # Bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        
        # Rook
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
                
        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
                
        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))

        

class Game:
    # Constructor
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
    
    # Rendering a field
    def field(self, surface):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row + col) % 2 == 0:
                    color = (234,235,200)
                else:
                    color = (119,154,88)
                    
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                
                pygame.draw.rect(surface, color, rect)
                
    # Render a game board with pieces
    def pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)