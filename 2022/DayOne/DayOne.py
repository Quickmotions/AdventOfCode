
def run(array):
    totals = []

    current = 0
    for calories in array:
        if calories is not None:
            current += calories
        else:
            totals.append(current)
            current = 0
    print(sorted(totals, reverse=True))
    top3total = 0
    for x in sorted(totals, reverse=True)[:3]:
        top3total += x
    print(top3total)


with open("DayOne/input.txt") as f:
    array = []
    for line in f.readlines():
        line = line.strip('\n')
        if line == '':
            array.append(None)
            continue
        array.append(int(line))
run(array)
