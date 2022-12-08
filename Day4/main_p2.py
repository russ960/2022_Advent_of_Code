count = 0
with open("Day4/input.txt", 'r') as f:
    section_clean = [value for value in f.read().strip().split("\n")]
        
for vals in section_clean:
    primary, secondary = vals.split(',')
    primary = [int(value) for value in primary.split('-')]
    secondary = [int(value) for value in secondary.split('-')]
    primary_range = range(primary[0],primary[1]+1)
    secondary_range = range(secondary[0], secondary[1]+1)
    primary_set = set(primary_range)
    intersection_out = primary_set.intersection(secondary_range)
    print(vals)
    print (intersection_out)
    if len(intersection_out) > 0:
        count += 1
print(count)

# x = range(1,10)
# y = range(8,20)
# xs = set(x)
# xs.intersection(y) 