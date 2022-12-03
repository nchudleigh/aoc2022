# A for Rock, B for Paper, and C for Scissors.
#  X for Rock, Y for Paper, and Z for Scissors.

# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).


game_map = {
    "R":  (1, "P", "R", "S"),
    "P":  (2, "S", "P", "R"),
    "S":  (3, "R", "S", "P"),
}

normalize = {
    "X": "R",
    "A": "R",
    "Y": "P",
    "B": "P",
    "Z": "S",
    "C": "S",
}

with open('./input.txt') as f:
    lines = f.readlines()
    games = []
    for line in lines:
        score = 0
        opp, outcome = line.strip("\n").split(" ")
        us = None
        # part 2
        # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
        opp = normalize[opp]

        if outcome == "X": # lose
            us = game_map[opp][3]
        elif outcome == "Y": # draw 
            us = game_map[opp][2]
        elif outcome == "Z": # win
            us = game_map[opp][1]
        
        choice_score, lose_condition, draw_condition, win_condition = game_map[us]

        score += choice_score
        if opp == draw_condition:
            score += 3
        elif opp == lose_condition:
            pass
        else:
            score += 6

        print(outcome, opp, us, score)

        games.append(score)
        
    print(games)
    print(sum(games))




            
