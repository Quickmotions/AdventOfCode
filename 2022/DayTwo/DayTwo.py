def run(array):
    score = 0
    new_array = []
    # meaning: 0 = lose, 1 = draw, 2 = win
    outcomes = [{"A": "Z", "B": "X", "C": "Y"}, {"A": "X", "B": "Y", "C": "Z"}, {"A": "Y", "B": "Z", "C": "X"}]
    for old in array:
        if old[2] == "X":
            new_array.append(old[0] + " " + outcomes[0][old[0]])
        elif old[2] == "Y":
            new_array.append(old[0] + " " + outcomes[1][old[0]])
        elif old[2] == "Z":
            new_array.append(old[0] + " " + outcomes[2][old[0]])

    outcomes = [{"X": 4, "Y": 8, "Z": 3}, {"X": 1, "Y": 5, "Z": 9}, {"X": 7, "Y": 2, "Z": 6 }]
    for strat in new_array:
        if strat[0] == "A":
            score += outcomes[0][strat[2]]
        elif strat[0] == "B":
            score += outcomes[1][strat[2]]
        elif strat[0] == "C":
            score += outcomes[2][strat[2]]
    print(score)

with open("input.txt") as f:
    array = []
    for line in f.readlines():
        array.append(line.strip('\n'))
run(array)