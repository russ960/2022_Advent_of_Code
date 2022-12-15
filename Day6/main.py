with open("Day6/input.txt", 'r') as f:
    data = f.readline()

def problem_1():
    max_value = 4
    min_value = 0
    no_good = 0
    for x in range(0,len(data)):
        test_range = data[min_value:max_value]
        for char in test_range:
            if test_range.count(char) >= 2:
                no_good = 1
                break
        if no_good == 1:
            no_good = 0
        else:
            print(max_value)
            break
        max_value += 1
        min_value += 1

def problem_2():
    max_value = 14
    min_value = 0
    no_good = 0
    for x in range(0,len(data)):
        test_range = data[min_value:max_value]
        for char in test_range:
            if test_range.count(char) >= 2:
                no_good = 1
                break
        if no_good == 1:
            no_good = 0
        else:
            print(max_value)
            break
        max_value += 1
        min_value += 1
        
problem_1()
problem_2()