priority_sum = 0
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

with open("Day3/input.txt", 'r') as f:
    for rucksack in f:
        mid_point = int(len(rucksack)/2)
        compartment_1 = set(rucksack[:mid_point])
        compartment_2 = set(rucksack[mid_point:])
        for item in compartment_1:
            if item in compartment_2:
                priority_sum += alpha.index(item) + 1
    print(priority_sum)
    