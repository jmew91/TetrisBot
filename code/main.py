from board import *
from piece import *

def generate_i_pieces():
    pieces = []
    pieces.append(Piece([
        [1],
        [1],
        [1],
        [1]
    ]))
    pieces.append(Piece([[1, 1, 1, 1]]))

    add_orientations(pieces)

    return pieces

def generate_j_pieces():
    pieces = []
    pieces.append(Piece([
        [0, 1],
        [0, 1],
        [1, 1]
    ]))
    pieces.append(Piece([
        [1, 0, 0],
        [1, 1, 1]
    ]))
    pieces.append(Piece([
        [1, 1],
        [1, 0],
        [1, 0]
    ]))
    pieces.append(Piece([
        [1, 1, 1],
        [0, 0, 1]
    ]))

    add_orientations(pieces)

    return pieces

def generate_l_pieces():
    pieces = []
    pieces.append(Piece([
        [1, 0],
        [1, 0],
        [1, 1]
    ]))
    pieces.append(Piece([
        [1, 1, 1],
        [1, 0, 0]
    ]))
    pieces.append(Piece([
        [1, 1],
        [0, 1],
        [0, 1]
    ]))
    pieces.append(Piece([
        [0, 0, 1],
        [1, 1, 1]
    ]))

    add_orientations(pieces)

    return pieces

def generate_o_pieces():
    pieces = []
    pieces.append(Piece([
        [1, 1],
        [1, 1]
    ]))

    add_orientations(pieces)

    return pieces

def generate_s_pieces():
    pieces = []
    pieces.append(Piece([
        [0, 1, 1],
        [0, 1, 0],
        [1, 1, 0]
    ]))
    pieces.append(Piece([
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 1]
    ]))

    add_orientations(pieces)

    return pieces

def generate_z_pieces():
    pieces = []
    pieces.append(Piece([
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]))
    pieces.append(Piece([
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 0]
    ]))

    add_orientations(pieces)

    return pieces

def generate_t_pieces():
    pieces = []
    pieces.append(Piece([
        [1, 1, 1],
        [0, 1, 0]
    ]))
    pieces.append(Piece([
        [0, 1],
        [1, 1],
        [0, 1]
    ]))
    pieces.append(Piece([
        [0, 1, 0],
        [1, 1, 1]
    ]))
    pieces.append(Piece([
        [1, 0],
        [1, 1],
        [1, 0]
    ]))

    add_orientations(pieces)

    return pieces

def add_orientations(pieces):
    for x in range(len(pieces)):
        piece = pieces[x]
        for y in range(1, len(pieces)):
            piece.add_orientation_piece(pieces[(x + y) % len(pieces)])

pieces = []

pieces.extend(generate_i_pieces())
pieces.extend(generate_j_pieces())
pieces.extend(generate_l_pieces())
pieces.extend(generate_o_pieces())
pieces.extend(generate_s_pieces())
pieces.extend(generate_z_pieces())
pieces.extend(generate_t_pieces())

for piece in pieces:
    print("New Piece:")
    piece.print()
    print()