from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, side, pos, string, state=True):
        self.side=side
        self.pos=pos
        self.string=string
        self.state=state # might be redundant as if the piece is not alive, then it won't be in the pieces dictionary
        self.possMoves=[]
        self.availPaths=[]
    
    @abstractmethod
    def possibleMoves(self, pieces):
        pass
    
    @abstractmethod
    def move(self, destination):
        pass
    
    def __str__(self):
        return self.string
    
class Pawn(Piece):
    # to code not moving through other pieces, make each move a combination of many moves if the move is more than one square away
    def possibleMoves(self, pieces):
        self.possMoves=[]
        self.availPaths=[]
        if self.side==1:
            self.availPaths.append([(self.pos[0],self.pos[1]+1)])
            self.availPaths.append([(self.pos[0]+1,self.pos[1]+1)])
            self.availPaths.append([(self.pos[0]-1,self.pos[1]+1)])
        elif self.side==-1:
            self.availPaths.append([(self.pos[0],self.pos[1]-1)])
            self.availPaths.append([(self.pos[0]+1,self.pos[1]-1)])
            self.availPaths.append([(self.pos[0]-1,self.pos[1]-1)])

        for i in self.availPaths:
            for c in pieces.keys():
                if c in i:
                    if pieces[c].side == self.side:
                        self.availPaths.remove(i)
                        break
                    elif pieces[c].side != self.side:
                        if i.index(c) != -1:
                            self.availPaths.remove(i)
                            break
                elif c not in i:
                    if i[-1][0]==self.pos[0]:
                        pass
                    elif i[-1][0]==self.pos[0]+1:
                        self.availPaths.remove(i)
                        break
                    elif i[-1][0]==self.pos[0]-1:
                        self.availPaths.remove(i)
                        break

        for i in self.availPaths:
            self.possMoves.append(i[-1])
            # for p in i:
            #     for c in pieces.keys():
            #         if p == c and self.side==pieces[c].side:
            #             availPaths.remove(i)
            #             break
            #         elif p == c and self.side!=pieces[c].side and availPaths.index(p) == -1:
            #             pass
            #         elif p == c and self.side!=pieces[c].side:
            #             availPaths.remove(i)
            #             break
            #         elif p != c:
            #             pass
        

                    # whole fuckin thing doesn't work. shit
                    # below if doesn't work, tries to only allow capture if the x-coord is different
                    # if ((i == c) and (self.side!=pieces[c].side)) and not(self.pos[0]==i[0]):
                    #     pass
                    # elif i == c and self.side==pieces[c].side:
                    #     self.possMoves.remove(i)
                    # elif i!=c and i[0]==c[0]:
                    #     pass
            

    
    def move(self, destination):
        self.pos=destination


class Rook(Piece):
    def possibleMoves(self, pieces):
        self.possMoves=[]
        self.availPaths=[]
        
        


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


if __name__ == "__main__":
    piece=TestPiece(1,1,1,True)
    piece.position()
    piece.move()
    piece.position()

    