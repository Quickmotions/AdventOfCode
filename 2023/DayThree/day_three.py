class Schematic:
    def __init__(self, matrix) -> None:
        self.array = matrix
        self.output = 0
        self.pointer_start = 0
        self.pointer_end = 0
        self.line = 0
        self.value = 0
        self.symbols = ["$", "#", "*", "%", "/", "&", ".", "+", "=", "-", "@"]
        self.special = ["$", "#", "*", "%", "/", "&", "+", "=", "-", "@"]
        self.complete = False

    def check_line_end(self):
        if self.pointer_start > len(self.array[self.line])-1:
            self.pointer_start = 0
            self.line += 1

    def next_value(self):
        try:
            self.pointer_start = self.pointer_end
            self.check_line_end()

            while self.array[self.line][self.pointer_start] in self.symbols:
                self.pointer_start += 1
                self.check_line_end()
            self.pointer_end = self.pointer_start

            while self.array[self.line][self.pointer_end] not in self.symbols:
                self.pointer_end += 1
                if self.pointer_end == len(self.array[self.line]):
                    break

            self.value = self.array[self.line][self.pointer_start:self.pointer_end]
            print(self.value, self.pointer_start, self.pointer_end)
        except IndexError:
            self.complete = True
        self.check_symbols()

    def check_symbols(self):
        found = False
        for pos in range(self.pointer_start, self.pointer_end):
            try:
                if self.array[self.line-1][pos-1] in self.special or \
                    self.array[self.line-1][pos] in self.special or \
                    self.array[self.line-1][pos+1] in self.special:
                    found = True
            except IndexError:
                continue
            try:
                if self.array[self.line+1][pos-1] in self.special or \
                    self.array[self.line+1][pos] in self.special or \
                    self.array[self.line+1][pos+1] in self.special:
                    found = True
            except IndexError:
                continue
            try:
                if self.array[self.line][pos+1] in self.special or \
                    self.array[self.line][pos-1] in self.special:
                    found = True
            except IndexError:
                continue
        if found:
            print(f"{self.value} is found")
            self.output += int(self.value)
        else:
            print(f"{self.value} is not found")


def run(data: list):
    schematic = Schematic(data)
    while not schematic.complete:
        schematic.next_value()
    print(schematic.output)

with open("2023/DayThree/input.txt") as f:
    array = []
    for line in f.readlines():
        line = line.strip('\n')
        if line == '':
            array.append(None)
            continue
        array.append(line)
run(array)
