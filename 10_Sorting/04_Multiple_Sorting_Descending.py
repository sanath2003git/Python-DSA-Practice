players = [
    ("Arun", 50),
    ("Bala", 80),
    ("Chetan", 80),
    ("Deep", 60)
]

players.sort(key=lambda x: (-x[1], x[0]))

print(players)