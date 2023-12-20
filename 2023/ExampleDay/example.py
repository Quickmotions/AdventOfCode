def run(data: list):
    ...


with open("2023/DayOne/input.txt") as f:
    array = []
    for line in f.readlines():
        line = line.strip('\n')
        if line == '':
            array.append(None)
            continue
        array.append(line)
run(array)
