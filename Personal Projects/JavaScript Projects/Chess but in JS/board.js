

class Board {
  constructor() {
    this.rowsInit = [[' *','  ',' *','  ',' *','  ',' *','  '],
    ['  ',' *','  ',' *','  ',' *','  ',' *'],
    [' *','  ',' *','  ',' *','  ',' *','  '],
    ['  ',' *','  ',' *','  ',' *','  ',' *'],
    [' *','  ',' *','  ',' *','  ',' *','  '],
    ['  ',' *','  ',' *','  ',' *','  ',' *'],
    [' *','  ',' *','  ',' *','  ',' *','  '],
    ['  ',' *','  ',' *','  ',' *','  ',' *']];
    this.rows = [...this.rowsInit];
    self.boardState = [[None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None]];
    self.showBoard();
  };
}