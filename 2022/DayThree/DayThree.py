def run(backpacks):
    sum = 0
    backpack_groups = []
    counter = 0
    while counter < len(backpacks) - 1:
        backpack_groups.append([list(backpacks[counter]), list(backpacks[counter+1]), list(backpacks[counter+2])])
        counter += 3

    for group in backpack_groups:
        common_char = set(group[0]).intersection(set(group[1]), set(group[2]))
        common_char = common_char.pop()
        if common_char.islower():
            sum += ord(common_char) - ord('a') + 1
        else:
            sum += ord(common_char) - ord('A') + 27
    return sum

with open("input.txt") as f:
    array = []
    for line in f.readlines():
        array.append(line.strip('\n'))
print(run(array))
