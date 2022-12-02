
def main():
    part_one()
    part_two()

def part_one():
    f = open("input.txt", "r")
    group_count = 0
    highest = 0
    for line in f:
        if line != "\n":
            group_count += int(line)
        else:
            if group_count > highest:
                highest = group_count
            group_count = 0
    print(highest)
    f.close()

def part_two():
    """ Heinously inefficient method """
    
    f = open("input.txt", "r")
    group_count = 0
    all_elves = []
    top_three = 0
    for line in f:
        if line != "\n":
            group_count += int(line)
        else:
            all_elves.append(group_count)
            group_count = 0
    all_elves.sort(reverse=True)
    for i in range(0,3):
        top_three += all_elves[i]
    print(top_three)
    f.close()

if __name__ == "__main__":
    main()