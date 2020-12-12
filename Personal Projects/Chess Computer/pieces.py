class Piece:
    possibleMoves=[]
    def __init__(self, side, pos, string, state=True):
        self.side=side
        self.pos=pos
        self.string=string
        self.state=state
    
    def possibleMoves(self):
        pass

    def position(self):
        print(self.x,self.y)
    
    def move(self, destination):
        if destination in self.possibleMoves:
            self.x=destination[0]
            self.y=destination[1]
        else:
            print('Uh oh, that\'s not a legal move, try again.')
    
    def __str__(self):
        return self.string
    
class Pawn(Piece):
    def possibleMoves(self):
        possibleMoves.append([self.x, self.y+1])
        possibleMoves.append([self.x+1, self.y+1])
        possibleMoves.append([self.x-1, self.y+1])

class Rook(Piece):
    def possibleMoves(self):
        possibleMoves.append([(self.x+1)%8, self.y])
        

class Knight:
    pass

class Bishop:
    pass

class Queen:
    pass

class King:
    pass

class TestPiece(Piece):
    def move(self, destination):
        self.pos=destination

        # start=input('Enter the square you are moving from: ')
        # start=start.split(' ')
        # start=[int(c) for c in start]
        # end=input('Enter the square you are moving to: ')
        # end=end.split(' ')
        # end=[int(i) for i in end]
        # val=True
        # while val:
        #     if 0<end[0]<9 and 0<end[1]<9:
        #         self.x=end[0]
        #         self.y=end[1]
        #         val=False
        #     else:
        #         inpt=input('Uh oh, that\'s not a legal move. Try again: ')
        #         inpt=inpt.split(' ')
        #         inpt=[int(i) for i in inpt]
        # # Board.update()# some way to find the name of the piece being moved


if __name__ == "__main__":
    piece=TestPiece(1,1,1,True)
    piece.position()
    piece.move()
    piece.position()

    