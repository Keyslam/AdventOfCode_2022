from dataclasses import dataclass


@dataclass
class Round:
    opponent_play: str
    own_play: str


def parse():
    rounds = []
    for line in open("input.txt", "r"):
        plays = line.split()
        rounds.append(Round(plays[0], plays[1]))
    return rounds


beats_map = {
    "rock": "scissor",
    "scissor": "paper",
    "paper": "rock",
}

beaten_map = {
    "scissor": "rock",
    "paper": "scissor",
    "rock": "paper",
}

score_map = {
    "rock": 1,
    "scissor": 3,
    "paper": 2,
}


def calculate_round_score(opponent_play, own_play):
    score = 0
    if opponent_play == own_play:  # Draw
        score += 3
    elif opponent_play == beats_map[own_play]:  # Win
        score += 6
    score += score_map[own_play]
    return score


def one():
    input_map = {
        "A": "rock",
        "B": "paper",
        "C": "scissor",
        "X": "rock",
        "Y": "paper",
        "Z": "scissor",
    }

    total_score = 0

    for round in parse():
        opponent_play = input_map[round.opponent_play]
        own_play = input_map[round.own_play]
        total_score += calculate_round_score(opponent_play, own_play)

    print(total_score)


def two():
    input_map = {
        "A": "rock",
        "B": "paper",
        "C": "scissor",
    }

    total_score = 0

    for round in parse():
        score = 0

        opponent_play = input_map[round.opponent_play]
        if round.own_play == "X":  # Need to lose
            own_play = beats_map[opponent_play]
        elif round.own_play == "Y":  # Need to draw
            own_play = opponent_play
        else:  # Need to win
            own_play = beaten_map[opponent_play]

        total_score += calculate_round_score(opponent_play, own_play)
    print(total_score)


if __name__ == '__main__':
    one()
    two()
