priority_sum = 0
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

with open("Day3/input.txt", 'r') as f:
    badge_priority_sum = 0
    elf_1 = []
    elf_2 = []
    elf_3 = []
    full_sack =  []
    current = 0
    for x in f:
        full_sack.append(x.strip())
    max_rows = len(full_sack)
    max_iter = int(max_rows/3)
    print(len(full_sack))
    for row_num in range(max_iter):
        print(f"{row_num} {current}")
        if current < max_rows:
            elf_1 = set(full_sack[current])
            current += 1
            elf_2 = full_sack[current]
            current += 1
            elf_3 = full_sack[current]
            current += 1
            print(elf_1)
            print(elf_2)
            print(elf_3)
            for item in elf_1:
                if item in elf_2 and item in elf_3:
                    print(item)
                    badge_priority_sum += alpha.index(item) + 1
    print(badge_priority_sum)


