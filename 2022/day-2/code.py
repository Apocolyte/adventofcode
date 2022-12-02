import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

data = []
with open("input.txt", "r") as f:
    data = [f.strip() for f in f.readlines()]

# A rock, B paper, C scissors
# X rock, Y paper, Z scissors
# Total score is sum of round scores
# Round score | (1 rock, 2 paper, 3 scissors) + round outcome (0 lost, 3 draw, 6 win)

total_score = 0
for round in data:
    round_score = 0
    round_parsed = round.split(" ")

    encode_opponent = {"A": 1, "B": 2, "C": 3}
    encode_player = {"X": 1, "Y": 2, "Z": 3}

    if encode_opponent[round_parsed[0]] == encode_player[round_parsed[1]]:
        # draw result
        round_score += (3 + encode_player[round_parsed[1]])
    
    elif encode_opponent[round_parsed[0]] + 1 == encode_player[round_parsed[1]]:
        # win result part 1
        round_score += (6 + encode_player[round_parsed[1]])

    elif encode_opponent[round_parsed[0]] == 3 and encode_player[round_parsed[1]] == 1:
        # win result part 2
        round_score += (6 + encode_player[round_parsed[1]])

    elif encode_opponent[round_parsed[0]] - 1 == encode_player[round_parsed[1]]:
        # lose result part 1
        round_score += encode_player[round_parsed[1]]

    elif encode_opponent[round_parsed[0]] == 1 and encode_player[round_parsed[1]] == 3:
        # lose result part 2
        round_score += encode_player[round_parsed[1]]

    total_score += round_score

# part 1
# print(total_score)

total_score = 0
for round in data:
    round_score = 0
    round_parsed = round.split(" ")

    encode_opponent = {"A": 1, "B": 2, "C": 3}
    encode_player = {"X": 1, "Y": 2, "Z": 3}

    if encode_player[round_parsed[1]] == 1:
        # lose result
        if encode_opponent[round_parsed[0]] == 1:
            round_score += (0 + 3) # edge case: rock requires scissors
        else:
            round_score += (0 + encode_opponent[round_parsed[0]] - 1)

    elif encode_player[round_parsed[1]] == 2:
        # draw result
        round_score += (3 + encode_opponent[round_parsed[0]])

    elif encode_player[round_parsed[1]] == 3:
        # win result
        if encode_opponent[round_parsed[0]] == 3:
            round_score += (6 + 1)
        else:
            round_score += (6 + encode_opponent[round_parsed[0]] + 1)

    total_score += round_score

print(total_score)
