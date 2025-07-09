import requests

FEN = "your_fen_string_here"
SIDE = "w"  # or "b" depending on user input
DEPTH = 12

url = f"https://stockfish.online/api/s/v2.php?fen={FEN}&depth={DEPTH}"
response = requests.get(url)
data = response.json()

best_move = data.get("bestmove")
print("Best move:", best_move)
