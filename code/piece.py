class Piece:
    def __init__(self, layout):
        self.layout = layout
        self.orientation_pieces = []

    def get_layout(self):
        return self.layout

    def get_orientation_pieces(self):
        return self.orientation_pieces

    def add_orientation_piece(self, piece):
        self.orientation_pieces.append(piece)

    def print(self):
        for i in range(len(self.layout)):
            print(' '.join(str(self.layout[i])))