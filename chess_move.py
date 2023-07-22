import requests

#get this move using youtube scrapper





#make chess move using lichess api
def make_chess_move (move):
    gameId = ""
    token = ""
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(f"https://lichess.org/api/board/game/{gameId}/move/{move}", headers=headers)

    print(response.status_code)
    