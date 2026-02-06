class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(game):
    rules = "RPSR"
    if len(game) == 2:
        move = "".join(list(zip(*game))[1])
        if all(c in rules for c in move):
            return " ".join(game[1] if move in rules else game [0])
        else:
            raise NoSuchStrategyError
    else:
        raise WrongNumberOfPlayersError
