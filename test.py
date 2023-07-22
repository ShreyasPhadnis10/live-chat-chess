# # # import chess

# # # board = chess.Board()

# # # # board.reset()
# # # # board.clear()

# # # def valid_chess_move (move):
    

# # #     legal_move = list(board.legal_moves)
# # #     print(legal_move)
# # #     if (chess.Move.from_uci(move) in legal_move):
# # #        print("It is a valud chess move", move)
# # #        board.push_uci(move)

# # #     else:
# # #         # return False
# # #         print("It is a invalid chess move")


# # # valid_chess_move("e2e4")

# # # valid_chess_move("h7h6")

# # # valid_chess_move("f1d3")

# # import chess

# # board = chess.Board()

# # # print(board)



# # # legal_move = list(board.legal_moves)

# # while not board.is_game_over():
# #     print(board)

# #     move = input("Enter your move: ")

# #     start = move[:2].upper()
# #     end = move[2:].upper()

# #     startMove = eval("chess." + start)
# #     endMove = eval("chess." + end)



# #     move = chess.Move(startMove, endMove)

# #     if board.is_legal(move):
# #         board.push(move)

# #     else:
# #         print("Invalid move")

    

    

# #     # push_move = chess.Move()

# #     # legal_move = list(board.legal_moves)

# #     # uci_move = chess.Move.from_uci(move)

# #     # if board.is_legal(uci_move):
# #     #     board.push(chess.E2, chess.E4)


# #     # startSquare = chess.E2
# #     # endSquare = chess.E4

# #     # move = chess.Move(startSquare, endSquare)

# #     # board.push(move)




# #     # if uci_move in legal_move:
# #     #     board.push(uci_move)

# #     # else:
# #     #     print("invalid move")

# # print("game over")

# # import requests

# # gameId = "cWaK4eeS"
# # token = "lip_q1wrkXvsqSTpCnzdjgKW"
# # headers = {"Authorization": f"Bearer {token}"}
# # url = f"https://lichess.org/api/stream/game/{gameId}"

# # reponse = requests.get(url, headers=headers)
# # print(reponse.status_code)
# # print(reponse.content)

# import json
# import websocket

# def on_message(ws, message):
#     message = json.loads(message)
#     if message['type'] == 'move':
#         print("Opponent's move:", message['move'])

# def on_error(ws, error):
#     print("Error:", error)

# def on_close(ws):
#     print("Connection closed")

# def on_open(ws):
#     ws.send(json.dumps({'t': 'sub', 'd': {'roomId': 'RAXGr0zy'}}))

# ws = websocket.WebSocketApp("wss://lichess.org/socket",
#                             on_message=on_message,
#                             on_error=on_error,
#                             on_close=on_close)
# ws.on_open = on_open
# ws.run_forever()

    