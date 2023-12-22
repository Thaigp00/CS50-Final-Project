CHESSBOARD_SIZE = 8

# For referencing each chessboard square.
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8']

PIECES_NAME = {'P': 'Pawn', 'R': 'Rook', 'H': 'Horse', 'B': 'Bishop', 'Q': 'Queen', 'K': 'King'}

PLAYER1 = input("Player 1: ")
PLAYER2 = input("Player 2: ")


def main():
    chessboard = create_chessboard()

    print()
    for acronym in PIECES_NAME:
        print(f"{acronym} - {PIECES_NAME[acronym]}")

    # Necessary variables.
    current_player = PLAYER1
    winner = 'NONE'
    eaten_piece = False
    old_piece, new_piece = False, False
    turn = 1

    # Main game.
    while True:
        if winner != 'NONE':
            print(f"\nThe game had {turn} turns.")
        else:
            print(f"\nTurn {turn}.")

        # Formatted print (between square brackets there's one space).
        print(f"[{'':^1}]", end=" ")
        for i in range(CHESSBOARD_SIZE):
            # Prints numbers (1 - 8).
            print(f"[{NUMBERS[i]:^1}]", end=" ")
        print()
        for i in range(CHESSBOARD_SIZE):
            # Prints letters (A - H).
            print(f"[{LETTERS[i]:^1}]", end=" ")
            for j in range(CHESSBOARD_SIZE):
                chessboard_square = chessboard[i][j]
                if chessboard_square['player'] == PLAYER1:
                    if is_light_color(i, j):
                        print(colored("light_green", f"[{chessboard_square['piece']:^1}]"), end=" ")
                    else:
                        print(colored("dark_green", f"[{chessboard_square['piece']:^1}]"), end=" ")
                elif chessboard_square['player'] == PLAYER2:
                    if is_light_color(i, j):
                        print(colored("light_red", f"[{chessboard_square['piece']:^1}]"), end=" ")
                    else:
                        print(colored("dark_red", f"[{chessboard_square['piece']:^1}]"), end=" ")
                else:
                    if is_light_color(i, j):
                        print(colored("light_neutral", f"[{'.':^1}]"), end=" ")
                    else:
                        print(colored("dark_neutral", f"[{'.':^1}]"), end=" ")
            print()

        if eaten_piece:
            if current_player == PLAYER1:
                print(colored("light_green", f"{PIECES_NAME[eaten_piece]}"), end="")
            else:
                print(colored("light_red", f"{PIECES_NAME[eaten_piece]}"), end="")
            print(" eaten.")

        # If a players' pawn reached the final of the chessboard (it may transform into a new piece).
        if new_piece:
            # Colors pieces names.
            if current_player == PLAYER2:
                colored_pawn = colored("light_green", "Pawn")
                colored_new_piece = colored("light_green", PIECES_NAME[new_piece])
            else:
                colored_pawn = colored("light_red", "Pawn")
                colored_new_piece = colored("light_red", PIECES_NAME[new_piece])

            print(f"The {colored_pawn} became a {colored_new_piece}.")

        if winner != 'NONE':
            print("The game is over!\n")
            break

        if current_player == PLAYER1:
            colored_player = colored("light_green", current_player)
        else:
            colored_player = colored("light_red", current_player)
        print(f"{colored_player}'s turn.\n")

        # Tries to get user's move until it is a valid move.
        while True:
            old_i, old_j, new_i, new_j = get_move()

            if not valid_square(chessboard, current_player, old_i, old_j, new_i, new_j):
                print("Invalid move.\n")
                continue

            valid_move, eaten_piece, winner, new_piece = \
                (update_chessboard(chessboard, current_player, old_i, old_j, new_i, new_j))
            if not valid_move:
                print("Invalid move.\n")
                continue
            break

        # Switches current player at the end of each turn.
        if current_player == PLAYER1:
            current_player = PLAYER2
        else:
            current_player = PLAYER1

        # Increases the turn counter at the end of each turn.
        if winner == 'NONE':
            turn += 1

    # Colors winner's name.
    if winner == PLAYER1:
        colored_player = colored("light_green", winner)
    else:
        colored_player = colored("light_red", winner)

    print(f"The winner was {colored_player}.")
    print("Congratulations!\n")


# Colors text.
def colored(color, text=""):
    match color:
        case "light_red":
            return f"\033[38;2;{255};{0};{0}m{text}\033[39m"
        case "dark_red":
            return f"\033[38;2;{180};{0};{0}m{text}\033[39m"
        case "light_green":
            return f"\033[38;2;{80};{255};{0}m{text}\033[39m"
        case "dark_green":
            return f"\033[38;2;{60};{180};{0}m{text}\033[39m"
        case "light_neutral":
            return f"\033[38;2;{230};{200};{100}m{text}\033[39m"
        case "dark_neutral":
            return f"\033[38;2;{180};{140};{70}m{text}\033[39m"


# Create the chessboard as a nested list.
# Each sublist in the list is a line of the chessboard.
# Each element of the sublist is a square of the chessboard.
# A square is represented as a dictionary containing:
#   -> The piece in the square (if there is a piece in the square, else it's NONE).
#   -> The player the piece belongs to (if there isn't a piece in the square, it's NONE).
#   -> If the piece was moved or not (Only for pawns, as it may move two squares at once only in the first move).
def create_chessboard():
    chessboard = []

    for i in range(CHESSBOARD_SIZE):
        chessboard_line = []
        for j in range(CHESSBOARD_SIZE):
            chessboard_square = {}

            if j == 0 or j == 1:
                chessboard_square['player'] = PLAYER1
            elif j == (CHESSBOARD_SIZE - 2) or j == (CHESSBOARD_SIZE - 1):
                chessboard_square['player'] = PLAYER2
            else:
                chessboard_square['player'] = 'NONE'

            if j == 1 or j == (CHESSBOARD_SIZE - 2):
                chessboard_square['piece'] = 'P'
                chessboard_square['moved'] = False
            elif j == 0 or j == (CHESSBOARD_SIZE - 1):
                if i == 0 or i == (CHESSBOARD_SIZE - 1):
                    chessboard_square['piece'] = 'R'
                elif i == 1 or i == (CHESSBOARD_SIZE - 2):
                    chessboard_square['piece'] = 'H'
                elif i == 2 or i == (CHESSBOARD_SIZE - 3):
                    chessboard_square['piece'] = 'B'
                elif i == 3:
                    chessboard_square['piece'] = 'Q'
                elif i == (CHESSBOARD_SIZE - 4):
                    chessboard_square['piece'] = 'K'
            else:
                chessboard_square['piece'] = 'NONE'

            chessboard_line.append(chessboard_square)
        chessboard.append(chessboard_line)

    return chessboard


def get_move():
    while True:
        indexes = []

        move = input("Your move: ")
        # Eliminates all spaces.
        move = move.replace(" ", "")

        # A valid move will always have length 4.
        if len(move) != 4:
            print("Invalid move.\n")
            continue

        # Get the positions.
        positions = [[move[0].upper(), move[1].upper()], [move[2].upper(), move[3].upper()]]
        valid_move = True

        # From now on, it checks whether the move is valid or not.
        # It is a very long part because I coded it to consider both '2B' and 'B2' valid.
        for position in positions:
            if len(position) != 2:
                print("Invalid move.\n")
                valid_move = False
                break

            if position[0] not in NUMBERS and position[0] not in LETTERS:
                print("Invalid move.\n")
                valid_move = False
                break

            elif position[0] in NUMBERS:
                if position[1].upper() not in LETTERS:
                    print("Invalid move.\n")
                    valid_move = False
                    break
                indexes.append(LETTERS.index(position[1].upper()))
                indexes.append(int(position[0]) - 1)

            elif position[0].upper() in LETTERS:
                if position[1] not in NUMBERS:
                    print("Invalid move.\n")
                    valid_move = False
                    break
                indexes.append(LETTERS.index(position[0].upper()))
                indexes.append(int(position[1]) - 1)

        if valid_move:
            return indexes


# True if the square with indexes i and j must have light color, else false.
def is_light_color(i, j):
    if (i + j) % 2 == 0:
        return True
    return False


# If the selected piece is not from current player or
# the destined square has a piece from the current player,
# it is an invalid move, else it is a valid move.
def valid_square(chessboard, current_player, old_i, old_j, new_i, new_j):
    if chessboard[old_i][old_j]['player'] != current_player:
        return False
    if chessboard[new_i][new_j]['player'] == current_player:
        return False
    return True


# Updates chessboard every turn.
def update_chessboard(chessboard, current_player, old_i, old_j, new_i, new_j, winner='NONE'):
    old_piece, new_piece = False, False

    # There's a function for every piece.
    # This match case statement chooses what function to use.
    match chessboard[old_i][old_j]['piece']:
        case 'P':
            valid_move, new_piece = pawn(chessboard, current_player, old_i, new_i, old_j, new_j)
            if not valid_move:
                return False, False, 'NONE', False
        case 'R':
            if not rook(chessboard, old_i, old_j, new_i, new_j):
                return False, False, 'NONE', False
        case 'H':
            if not horse(old_i, old_j, new_i, new_j):
                return False, False, 'NONE', False
        case 'B':
            if not bishop(chessboard, old_i, old_j, new_i, new_j):
                return False, False, 'NONE', False
        case 'Q':
            if not queen(chessboard, old_i, old_j, new_i, new_j):
                return False, False, 'NONE', False
        case 'K':
            if not king(old_i, old_j, new_i, new_j):
                return False, False, 'NONE', False

    if chessboard[new_i][new_j]['player'] == 'NONE':
        piece_acronym = False
    else:
        # New square having a piece means that the piece will be eaten.
        piece_acronym = chessboard[new_i][new_j]['piece']

        # If the eaten piece is the king, already decides the winner (current player).
        if piece_acronym == 'K':
            winner = current_player

    # The square that used to be the piece will now be an empty square.
    # And the piece will go to the destined square.
    chessboard[old_i][old_j], chessboard[new_i][new_j] = {'player': 'NONE', 'piece': 'NONE'}, chessboard[old_i][old_j]

    return True, piece_acronym, winner, new_piece


# Check if the pawn's move is valid
def pawn(chessboard, current_player, old_i, new_i, old_j, new_j):
    if chessboard[new_i][new_j]['player'] == 'NONE':
        eating = False
    else:
        eating = True

    if old_i != new_i and not eating:
        return False, False
    if abs(old_i - new_i) != 1 and eating:
        return False, False

    if current_player == PLAYER1:
        if not chessboard[old_i][old_j]['moved']:
            if (new_j - old_j) not in [1, 2] and not eating:
                return False, False
            if (new_j - old_j) != 1 and eating:
                return False, False
            if (new_j - old_j) == 2 and chessboard[old_i][old_j + 1]['piece'] != 'NONE':
                return False, False
            chessboard[old_i][old_j]['moved'] = True
        else:
            if (new_j - old_j) != 1:
                return False, False
    else:
        if not chessboard[old_i][old_j]['moved']:
            if (old_j - new_j) not in [1, 2] and not eating:
                return False, False
            if (old_j - new_j) != 1 and eating:
                return False, False
            if (old_j - new_j) == 2 and chessboard[old_i][old_j - 1]['piece'] != 'NONE':
                return False, False
            chessboard[old_i][old_j]['moved'] = True
        else:
            if (old_j - new_j) != 1:
                return False, False

    new_piece = False

    # If pawn reached end of chessboard (it may change into a new piece).
    if (current_player == PLAYER1 and new_j == (CHESSBOARD_SIZE - 1)) or (current_player == PLAYER2 and new_j == 0):
        while True:
            selected_piece = input("Desired piece: ")

            # It works both for acronym and full name (for example, it works both for 'R' and 'Rook').
            if selected_piece.upper() in PIECES_NAME.keys() and selected_piece.upper() != 'P':
                break
            if selected_piece.capitalize() in PIECES_NAME.values() and selected_piece.capitalize() != 'Pawn':
                break

            # If it is not a valid piece (it will loop again until it is a valid piece).
            print("\nInvalid piece.\n")

        chessboard[old_i][old_j]['piece'] = selected_piece[0].upper()
        new_piece = selected_piece[0].upper()

    return True, new_piece


# Check if the rook's move is valid
def rook(chessboard, old_i, old_j, new_i, new_j):
    if old_i != new_i and old_j != new_j:
        return False

    piece_between = False
    if new_i > old_i:
        for inc in range(1, (new_i - old_i)):
            if chessboard[old_i + inc][old_j]['piece'] != 'NONE':
                piece_between = True
                break

    elif new_i < old_i:
        for inc in range(1, (old_i - new_i)):
            if chessboard[old_i - inc][old_j]['piece'] != 'NONE':
                piece_between = True
                break

    elif new_j > old_j:
        for inc in range(1, (new_j - old_j)):
            if chessboard[old_i][old_j + inc]['piece'] != 'NONE':
                piece_between = True
                break

    elif new_j < old_j:
        for inc in range(1, (old_j - new_j)):
            if chessboard[old_i][old_j - inc]['piece'] != 'NONE':
                piece_between = True
                break

    # A rook cannot go to a square if there is a piece between its current square and its destined square.
    # The only piece that may "jump" through pieces is the horse.
    if piece_between:
        return False

    return True


# Check if the horse's move is valid
def horse(old_i, old_j, new_i, new_j):
    valid_move = False

    if abs(old_i - new_i) == 2:
        if abs(old_j - new_j) == 1:
            valid_move = True
        else:
            return False

    if abs(old_i - new_i) == 1:
        if abs(old_j - new_j) == 2:
            valid_move = True
        else:
            return False

    if not valid_move:
        return False

    return True


# Check if the bishop's move is valid
def bishop(chessboard, old_i, old_j, new_i, new_j):
    if abs(new_i - old_i) != abs(new_j - old_j):
        return False
    length = abs(new_i - old_i)

    piece_between = False
    if new_i > old_i and new_j > old_j:
        for inc in range(1, length):
            if chessboard[old_i + inc][old_j + inc]['piece'] != 'NONE':
                piece_between = True
                break

    elif new_i < old_i and new_j > old_j:
        for inc in range(1, length):
            if chessboard[old_i - inc][old_j + inc]['piece'] != 'NONE':
                piece_between = True
                break

    elif new_i > old_i and new_j < old_j:
        for inc in range(1, length):
            if chessboard[old_i + inc][old_j - inc]['piece'] != 'NONE':
                piece_between = True
                break

    elif new_i < old_i and new_j < old_j:
        for inc in range(1, length):
            if chessboard[old_i - inc][old_j - inc]['piece'] != 'NONE':
                piece_between = True
                break

    if piece_between:
        return False

    return True


# Check if the queen's move is valid
def queen(chessboard, old_i, old_j, new_i, new_j):
    while True:
        if (new_i == old_i and new_j != old_j) or (new_i != old_i and new_j == old_j):
            mode = "R"
            break

        if abs(new_i - old_i) == abs(new_j - old_j):
            mode = "B"
            break

        return False

    # The queen has the functionalities of a rook and a bishop combined,
    # so I just analyse in which mode the queen is moving and use the corresponding function.
    if mode == "R":
        return rook(chessboard, old_i, old_j, new_i, new_j)

    elif mode == "B":
        return bishop(chessboard, old_i, old_j, new_i, new_j)

# Check if the king's move is valid
def king(old_i, old_j, new_i, new_j):
    if abs(old_i - new_i) > 1 or abs(old_j - new_j) > 1:
        return False


# Executes the main function.
main()
