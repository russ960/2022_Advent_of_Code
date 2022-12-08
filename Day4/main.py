count = 0
with open("Day4/input.txt", 'r') as f:
    section_clean = [value for value in f.read().strip().split("\n")]
        
for vals in section_clean:
    primary, secondary = vals.split(',')
    primary = [int(value) for value in primary.split('-')]
    secondary = [int(value) for value in secondary.split('-')]
    if primary[0] <= secondary[0] and primary[1] >= secondary[1]:
        count += 1
        print(f"{primary[0]}-{primary[1]}  {secondary[0]}-{secondary[1]}")
    elif secondary[0] <= primary[0] and secondary[1] >= primary[1]:
        count += 1
        print(f"{primary[0]}-{primary[1]}  {secondary[0]}-{secondary[1]}")
print(count)