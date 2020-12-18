from board import *
from pieces import *

board=Board()
wp1=Pawn(1,(4,7),'wp',True)
bp1=Pawn(-1,(5,3),'bp',True)
board.addPiece(wp1)
board.addPiece(bp1)
board.update()
while True:
    board.move()
