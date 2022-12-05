outcomes_values = {
    'A X':4, # Rock
    'B Y':5, # Paper
    'C Z':6, # Scissors
    'A Y':8,
    'A Z':3,
    'B X':1,
    'B Z':9,
    'C X':7,
    'C Y':2
}
tie_values = {
    'A':4,
    'B':5,
    'C':6}

win_values = {
    'A':8,
    'B':9,
    'C':7
}

loss_values = {
    'A':3,
    'B':1,
    'C':2
}

score = 0

with open("Day2/input.txt", 'r') as f:
    outcomes_list = []
    myset = set(outcomes_list)
    print(myset)
    for row in f:
        outcomes_list.append(row.strip())
    for key_value in outcomes_list:
        if key_value[2] == 'X':
            score += loss_values[key_value[0]]
            print (loss_values[key_value[0]])
        elif key_value[2] == 'Y':
            score += tie_values[key_value[0]]
            print (tie_values[key_value[0]])
        elif key_value[2] == 'Z':
            score += win_values[key_value[0]]
            print (win_values[key_value[0]])
print(score)