import string
import re

sets = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def run(data: list):
    output = []
    for word in data:
        print(word)
        for letters, number in sets.items():
            x = re.search(letters, word)
            while x:
                word = word[:x.start()+1] + str(number) + word[x.start()+1:]
                x = re.search(letters, word)

        word = re.sub(f"[{string.ascii_letters}]", "", word)
        print(word)
        output.append(int(word[0]+word[-1]))

    print(sum(output))


with open("2023/DayOne/input.txt") as f:
    array = []
    for line in f.readlines():
        line = line.strip('\n')
        if line == '':
            array.append(None)
            continue
        array.append(line)
run(array)
