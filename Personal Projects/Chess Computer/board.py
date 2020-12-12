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
        self.pieces={}
        self.showBoard()
        
    def update(self):
        self.rows=deepcopy(self.rowsInit)
        for piece in self.pieces.values():
            x=piece.pos[0]-1
            y=piece.pos[1]-1
            self.rows[x][y]=str(piece)
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

    def addPiece(self, piece):
        self.pieces[piece.pos]=piece

    def move(self):
        pos=input('Enter the position of the piece you would like to move: ')
        pos=pos.split(',')
        pos=tuple(int(c) for c in pos)
        val=True
        while val:
            if pos in self.pieces.keys():
                destination=input('Enter the destination: ')
                destination=destination.split(',')
                destination=tuple(int(c) for c in destination)
                self.pieces[pos].move(destination)
                self.pieces[destination]=self.pieces.pop(pos)
                self.update()
                val=False
            else:
                pos=input('There is no piece at that position, try again: ')
                pos=pos.split(',')
                pos=tuple(int(c) for c in pos)


if __name__ == "__main__":
    board=Board()