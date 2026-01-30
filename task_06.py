class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(list):
    if len(list) == 2:
        p1 = list[0]
        p2 = list[1]
        p1_choice = list[0][1]
        p2_choice = list[1][1]
        if (p1_choice in ("R", "P", "S") and p2_choice in ("R", "P", "S")):
            if p1_choice == p2_choice:
                return " ".join(p1)
            if p1_choice == "R" and p2_choice == "S":
                return " ".join(p1)
            if p1_choice == "R" and p2_choice == "P":
                return " ".join(p2)
            if p1_choice == "P" and p2_choice == "R":
                return " ".join(p1)
            if p1_choice == "P" and p2_choice == "S":
                return " ".join(p2)
            if p1_choice == "S" and p2_choice == "P":
                return " ".join(p1)
            if p1_choice == "S" and p2_choice == "R":
                return " ".join(p2)
        else:
            raise NoSuchStrategyError
    else:
        raise WrongNumberOfPlayersError
