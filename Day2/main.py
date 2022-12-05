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
score = 0

with open("Day2/input.txt", 'r') as f:
    outcomes_list = []
    myset = set(outcomes_list)
    print(myset)
    for row in f:
        outcomes_list.append(row.strip())
    for key_value in list(outcomes_values.keys()):
        count = outcomes_list.count(key_value)
        print(f"{outcomes_values[key_value]} : {key_value} : {count} : {outcomes_values[key_value] * count}")
        score += outcomes_values[key_value] * count
        count = 0

print(score)