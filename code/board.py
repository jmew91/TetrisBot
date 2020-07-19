class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0 for x in range(rows)] for y in range(cols)] 

    def print_board(self):
        print(self.rows)