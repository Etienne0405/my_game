from utils.typewriter import typewriter
from systems.inventory import inventory

import time
import chess
import random


piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

OPENING_BOOK = [
    "e2e4", "d2d4", "c2c4", "g1f3",   # strong first moves
    "b1c3", "f2f4", "e2e3", "d2d3"
]
# needs quotation marks
GHOST_TAUNTS = {
    "winning": [
        '"Your pieces tremble…"',
        '"I can already see your king falling."',
        '"You should have stayed in the dark."',
        '"Your position is collapsing…"',
        '"Every move you make is a mistake."'
    ],
    "losing": [
        '"No… that move was not supposed to happen."',
        '"You are stronger than I thought…"',
        '"The board is turning against me."',
        '"This is… inconvenient."',
        '"I don\'t like where this is going…"'
    ],
    "even": [
        '"Interesting…"',
        '"You are holding up well."',
        '"Let us see who breaks first."',
        '"The tension is delicious…"',
        '"Neither of us dares blink."'
    ]
}

def ghost_talk(board):
    score = evaluate(board)

    if score < -200:
        mood = "winning"
    elif score > 200:
        mood = "losing"
    else:
        mood = "even"

    line = random.choice(GHOST_TAUNTS[mood])
    typewriter(f"\n{line}\n")

def draw_board(board):
    piece_map = {
        "P": "♙", "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔",
        "p": "♟", "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚",
        ".": "·"
    }

    last_move = board.peek() if board.move_stack else None
    highlight_squares = set()

    if last_move:
        highlight_squares.add(last_move.from_square)
        highlight_squares.add(last_move.to_square)

    print("\n   a  b  c  d  e  f  g  h")

    for rank in range(7, -1, -1):
        print(" " + str(rank + 1), end=" ")

        for file in range(8):
            square = chess.square(file, rank)
            piece = board.piece_at(square)
            char = piece.symbol() if piece else "."
            symbol = piece_map[char]

            if square in highlight_squares:
                # red background
                print(f"\033[41m{symbol}\033[0m", end="  ")
            else:
                print(symbol, end="  ")

        print(" " + str(rank + 1))

    print("   a  b  c  d  e  f  g  h\n")


def evaluate(board):
    if board.is_checkmate():
        return -99999 if board.turn else 99999
    if board.is_stalemate():
        return 0

    score = 0

    # Material
    for piece_type, value in piece_values.items():
        score += len(board.pieces(piece_type, chess.WHITE)) * value
        score -= len(board.pieces(piece_type, chess.BLACK)) * value

    # Center control
    center_squares = [chess.D4, chess.E4, chess.D5, chess.E5]
    for sq in center_squares:
        if board.is_attacked_by(chess.WHITE, sq):
            score += 20
        if board.is_attacked_by(chess.BLACK, sq):
            score -= 20

    # Development (penalize undeveloped pieces early)
    if board.fullmove_number <= 10:
        for piece in [chess.BISHOP, chess.KNIGHT]:
            score -= 15 * len(board.pieces(piece, chess.BLACK) & chess.SquareSet(chess.BB_BACKRANKS))
            score += 15 * len(board.pieces(piece, chess.WHITE) & chess.SquareSet(chess.BB_BACKRANKS))

    # King safety (encourage castling)
    if board.fullmove_number <= 15:
        # White castling potential
        if not (board.has_kingside_castling_rights(chess.WHITE) or board.has_queenside_castling_rights(chess.WHITE)):
            score -= 30  # White has already castled or lost rights

        # Black castling potential
        if not (board.has_kingside_castling_rights(chess.BLACK) or board.has_queenside_castling_rights(chess.BLACK)):
            score += 30  # Black has already castled or lost rights


    return score



def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing:
        max_eval = -999999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = 999999
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def get_ai_move(board):
    # Use opening book in early game
    if board.fullmove_number <= 3:
        book_moves = [m for m in board.legal_moves if m.uci() in OPENING_BOOK]
        if book_moves:
            return random.choice(book_moves)

    best_move = None
    best_value = 999999
    recent_moves = [m.uci() for m in board.move_stack[-4:]]

    for move in board.legal_moves:
        penalty = 30 if move.uci() in recent_moves else 0

        board.push(move)
        value = minimax(board, 2, -999999, 999999, True)
        board.pop()

        value += penalty

        if value < best_value:
            best_value = value
            best_move = move

    return best_move

def play_chess():
    board = chess.Board()

    typewriter("The moment you touch the chessboard, you are drawn to it...\n")
    typewriter("A ghostly opponent materializes across from you, challenging you to a game of chess.\n")
    time.sleep(1)
    typewriter('"If you can defeat me, I shall give you a precious item," the ghost whispers.\n')
    time.sleep(1)

    typewriter("To play chess. Enter moves like: e2e4 or g1f3.")
    typewriter("To promote a pawn, append the piece letter: e7e8[letter]. [letter]=q, r, b, n.")
    typewriter("Castling is done by moving the king 2 squares.")
    typewriter("Type 'quit' to leave the board.\n")

    

    while not board.is_game_over():
        draw_board(board)

        # Player move
        move = input("\nYour move: ").strip().lower()

        if move == "quit":
            typewriter("You step away from the chessboard...\n")
            return

        try:
            board.push_uci(move)
        except:
            typewriter("That move is not allowed.\n")
            continue

        # Check if player won
        if board.is_checkmate():
            draw_board(board)
            typewriter("\nThe ghost stares in disbelief...")
            typewriter("You won the game.\n")
            if "pistol" not in inventory:
                typewriter('"Congratulations, brave soul," the ghost says softly.')
                typewriter('"Take this pistol as a reward for your victory."')
                typewriter("The ghost hands you a pistol before vanishing.\n")
                inventory.append("pistol")
            else:
                typewriter('"You have already claimed your reward," the ghost murmurs before fading away.\n')

            typewriter("The chessboard fades into dust...\n")
            return

        # AI move
        typewriter("The ghost is thinking...\n")
        ai_move = get_ai_move(board)
        board.push(ai_move)

        typewriter(f"\nThe ghost moves: {ai_move}\n")
        ghost_talk(board)

        if board.is_checkmate():
            draw_board(board)
            typewriter("\nThe ghost lets out a hollow laugh...")
            typewriter("You have been defeated.\n")
            typewriter("The chessboard vanishes.\n")
            return
