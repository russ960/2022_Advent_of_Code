count = 0
with open("Day4/input.txt", 'r') as f:
    for section in f:
        section_clean = section.strip()
        primary, secondary = section_clean.split(',')
        primary = primary.split('-')
        secondary = secondary.split('-')
        if secondary[0] >= primary[0] and secondary[1] <= primary[1]:
            count += 1
        # elif primary[0] >= secondary[0] and primary[1] <= secondary[1]:
        #     count += 1
    print(count)