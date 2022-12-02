totals = []
sum_elf = 0
with open("Day1/input.txt", 'r') as f:
    for current in f.readlines():
        if current == '\n':
            totals.append(sum_elf)
            sum_elf = 0
        else:
            sum_elf += int(current)
totals.sort(reverse=True)
print(sum(totals[:3]))
