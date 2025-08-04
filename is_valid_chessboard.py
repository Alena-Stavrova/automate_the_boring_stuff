#Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on whether the board is valid.

#A valid board will have exactly one black king and exactly one white king.
#Each player can have at most 16 pieces, of which only eight can be pawns, and all pieces must be on a valid square from '1a' to '8h'. That is, a piece can’t be on square '9z'.
#The piece names should begin with either a 'w' or a 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
#This function should detect when a bug has resulted in an improper chessboard. (This isn’t an exhaustive list of requirements, but it is close enough for this exercise.)

def isValidChessBoard(dict):
    bk_count = 0 #Black King counter
    for v in dict.values():
        if v == 'bK':
            bk_count += 1

    wk_count = 0 #White King counter
    for v in dict.values():
        if v == 'wK':
            wk_count += 1

    bp_count = 0 #Black pieces counter
    for v in dict.values():
        if v[0] == 'b':
            bp_count += 1

    wp_count = 0 #White pieces counter
    for v in dict.values():
        if v[0] == 'w':
            wp_count += 1

    bpawn_count = 0 #Black pawn counter
    for v in dict.values():
        if v[0] == 'bP':
            bpawn_count += 1

    wpawn_count = 0 #White pawn counter
    for v in dict.values():
        if v[0] == 'wP':
            wpawn_count += 1

    wrong_keys = 0
    for k in dict.keys(): #Wrong key counter
        if k[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] or k[1] not in ['1', '2', '3', '4', '5', '6', '7', '8'] or len(k) > 2: #Many ways for the key to be incorrect, but for simplicity I excluded letters after 'h', number '9' and 3+ symbols.
            wrong_keys += 1

    wrong_values = 0
    for v in dict.values(): #Wrong value counter
        if v[0] not in ['w', 'b'] or v[1] not in ['P', 'N', 'B','R', 'Q', 'K'] or len(v) >2:
            print(v[0], v[1])
            wrong_values += 1

    if bk_count != 1 or wk_count != 1 or bp_count > 16 or wp_count > 16 or bpawn_count > 8 or wpawn_count > 8 or wrong_keys !=0 or wrong_values != 0:
        return False
    else:
        return True

my_chessboard = {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'}
print(isValidChessBoard(my_chessboard))
