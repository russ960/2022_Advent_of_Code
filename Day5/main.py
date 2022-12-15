def process_moves(loading_list, move_list):
    for move in move_list:
        move_quantity = int(move[0])
        move_from = int(move[1])-1
        move_to = int(move[2])-1
        for m in range(0,move_quantity):
            popped_val = loading_list[move_from].pop(0)
            loading_list[move_to].insert(0, popped_val)
    return loading_list

# Build the 2 lists
with open("Day5/input.txt", 'r') as f:
    data = [value for value in f.read().split("\n")]
ship_load = []
move_instructions = []
for x in data:
    if x != '' and x[0:4] != 'move':
        ship_load.append(x)
    elif x != '' and x[0:4] == 'move':
        move_instructions.append(x)
column_numbers = ship_load.pop(len(ship_load)-1)
number_of_columns = int(column_numbers[len(column_numbers)-2])
level = 0

workload = [[] for x in range(0,number_of_columns)]

for x in ship_load:
    working_list = []
    for n in range(len(x)):
        if n == 1 or n % 4 == 1:
            working_list.append(x[n])
    #workload.append(working_list)
    for y in range(0,number_of_columns):
        if working_list[y] != ' ':
            workload[y].append(working_list[y])
    level += 1

print(workload)

move_instructions_converted = [move.replace('move ','').replace('from ','').replace('to ','').split(' ') for move in move_instructions]
new_workload = process_moves(workload, move_instructions_converted)

for x in new_workload:
    print(x[0])