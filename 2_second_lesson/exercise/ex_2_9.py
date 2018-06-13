def duck_duck_goose(players, goose):
    return players[goose % len(players) - 1]


players = ['a', 'b', 'c', 'd']
goose = 4
