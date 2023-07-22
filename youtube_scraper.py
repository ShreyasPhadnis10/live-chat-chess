import pytchat
import re
# import chess
from chess_move import make_chess_move

# Create a chat object to retrieve live chat messages from a YouTube video with the given video_id
chat = pytchat.create(video_id="bT6j4KLURB4")

# Initialize an empty variable to store the chess move
move = ""

# Define a function to check the validity of the chess move entered by the user
def validity(move):
    # Define a regular expression pattern to match a valid chess move in the format "e2e4"
    pattern = re.compile("^[a-h][1-8][a-h][1-8]$")

    # Check if the move matches the defined pattern
    if pattern.match(move):
        # If the move is valid, call the make_chess_move function with the move as an argument to process it
        make_chess_move(move)
        print("Move made")
    else:
        # If the move is invalid, print an error message
        print("Invalid input")

# Main loop to continuously read chat messages and process chess moves
while chat.is_alive():
    for c in chat.get().sync_items():
        # Check if the chat message contains exactly 4 characters, which indicates a potential chess move
        if len(c.message) == 4:
            print(c.message)
            # Call the validity function to check if the move is valid and process it if it is
            validity(c.message)

# The code for handling the chess board and checking for valid chess moves is currently commented out,


# def valid_chess_move(move):
#     # Define a list of legal chess moves
#     legal_move = list(board.legal_moves)
#     # Check if the move is in the list of legal moves
#     if chess.Move.from_uci(move) in legal_move:
#         print("It is a valid chess move")
#         board.push_uci(move)
#     else:
#         print("It is an invalid chess move")


