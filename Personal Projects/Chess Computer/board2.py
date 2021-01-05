from copy import deepcopy


class Board:
    """
    Board has a list of all the pieces on the board, which are all Piece objects
    """
    def __init__(self):
        self.rowsInit=[[' *','  ',' *','  ',' *','  ',' *','  '],
        ['  ',' *','  ',' *','  ',' *','  ',' *'],
        [' *','  ',' *','  ',' *','  ',' *','  '],
        ['  ',' *','  ',' *','  ',' *','  ',' *'],
        [' *','  ',' *','  ',' *','  ',' *','  '],
        ['  ',' *','  ',' *','  ',' *','  ',' *'],
        [' *','  ',' *','  ',' *','  ',' *','  '],
        ['  ',' *','  ',' *','  ',' *','  ',' *']]
        self.rows=deepcopy(self.rowsInit)
        self.boardState=[[None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None]]
        self.pieces={}
        self.showBoard()
        
    def update(self):
        self.rows=deepcopy(self.rowsInit)
        for y, i in enumerate(self.boardState):
            for x, c in enumerate(i):
                if c:
                    self.rows[c.pos[1]-1][c.pos[0]-1]=str(c)
                else:
                    self.rows[y][x]=self.rowsInit[y][x]
        self.showBoard()
    
    def showBoard(self):
        print('|{}|{}|{}|{}|{}|{}|{}|{}|'.format(*self.rows[7]))
        print('|{}|{}|{}|{}|{}|{}|{}|{}|'.format(*self.rows[6]))
        print('|{}|{}|{}|{}|{}|{}|{}|{}|'.format(*self.rows[5]))
        print('|{}|{}|{}|{}|{}|{}|{}|{}|'.format(*self.rows[4]))
        print('|{}|{}|{}|{}|{}|{}|{}|{}|'.format(*self.rows[3]))
        print('|{}|{}|{}|{}|{}|{}|{}|{}|'.format(*self.rows[2]))
        print('|{}|{}|{}|{}|{}|{}|{}|{}|'.format(*self.rows[1]))
        print('|{}|{}|{}|{}|{}|{}|{}|{}|'.format(*self.rows[0]))
        print()

    def addPiece(self, piece):# maybe use pos as an argument for addPiece, remove it from Piece? not sure about that
        self.boardState[piece.pos[1]-1][piece.pos[0]-1]=piece

    def move(self):
        pos=input('Enter the position of the piece you would like to move: ')
        pos=pos.split(',')
        pos=tuple(int(c) for c in pos)
        valPos=True
        while valPos:
            piece=self.boardState[pos[1]-1][pos[0]-1]
            if piece:
                piece.possibleMoves(self.boardState)
                destination=input('Enter the destination: ')
                destination=destination.split(',')
                destination=tuple(int(c) for c in destination)
                valDest=True
                while valDest:
                    if destination in piece.possMoves:
                        piece.move(destination)
                        self.boardState[pos[1]-1][pos[0]-1] = None
                        self.boardState[destination[1]-1][destination[0]-1] = piece
                        valDest=False
                    else: 
                        destination=input('That is not a legal move, try again: ')
                        destination=destination.split(',')
                        destination=tuple(int(c) for c in destination)
                valPos=False
            else:
                pos=input('There is no piece at that position, try again: ')
                pos=pos.split(',')
                pos=tuple(int(c) for c in pos)


if __name__ == "__main__":
    board=Board()