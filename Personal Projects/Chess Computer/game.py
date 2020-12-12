from board import *
from pieces import *

board=Board()
piece=TestPiece(1,(1,1),'wQ',True)
board.addPiece(piece)
board.update()
board.move()
board.update()
