item_value = {'X':1, 'Y':2, 'Z':3}
score = 0

with open("Day2/input.txt", 'r') as f:
    for bet in f.readlines():
        if bet[0] == 'A' and bet[2] == 'X':
            score += 3 + item_value['X']
        elif bet[0] == 'B' and bet[2] == 'Y':
            score += 3 + item_value['Y']
        elif bet[0] == 'C' and bet[2] == 'Z':
            score += 3 + item_value['Z']
        elif bet[0] == 'A' and bet[2] == 'Y':
            score += 6 + item_value['Y']
        elif bet[0] == 'A' and bet[2] == 'Z':
            score += item_value['Z']
        elif bet[0] == 'B' and bet[2] == 'X':
            score += item_value['X']
        elif bet[0] == 'B' and bet[2] == 'Z':
            score += 6 + item_value['Z']
        elif bet[0] == 'C' and bet[2] == 'X':
            score += item_value['X']
        elif bet[0] == 'C' and bet[2] == 'Y':
            score += 6 + item_value['Y']
print(score)