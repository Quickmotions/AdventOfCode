class Game:
    def __init__(self, number) -> None:
        self.num = number
        self.blue = 0
        self.red = 0
        self.green = 0
        self.possible = True

    def add_red(self, amount):
        if amount > self.red:
            self.red = amount

    def add_green(self, amount):
        if amount > self.green:
            self.green = amount

    def add_blue(self, amount):
        if amount > self.blue:
            self.blue = amount

    def is_possible(self):
        if self.red > 12 or self.green > 13 or self.blue > 14:
            self.possible = False
        if self.possible:
            return self.num
        else:
            return 0


def run(data: list):
    output = 0
    for game in data:
        number, plays = game.split(":")
        print(number)

        current_game = Game(int(number.split(" ")[1]))
        for play in plays.split(";"):
            for cubes in play.split(","):
                print(cubes)
                unused_space, amount, colour = cubes.split(" ")
                if colour == "red":
                    current_game.add_red(int(amount))
                if colour == "blue":
                    current_game.add_blue(int(amount))
                if colour == "green":
                    current_game.add_green(int(amount))
        power = int(current_game.red)*int(current_game.blue)*int(current_game.green)
        output += power

    print(f"total: {output}")


with open("2023/DayTwo/input.txt") as f:
    array = []
    for line in f.readlines():
        line = line.strip('\n')
        if line == '':
            array.append(None)
            continue
        array.append(line)
run(array)
