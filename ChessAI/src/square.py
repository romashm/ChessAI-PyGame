
class Square:
    # Receiver values
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        
    # Condition if this place has a piece
    def has_piece(self):
        return self.piece != None